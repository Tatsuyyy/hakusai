window.onload = () => {
  registerFromEvent();
  registerButtonEvents();
  registerStepOperations();
};

const getStepCount = () => {
  const parent = document.getElementById("js-step-parent");
  return parent.children.length - 1;
};

const registerFromEvent = () =>{
  const formElement = document.getElementById("js-step-form")
  formElement.addEventListener("submit", (event) => {
    const submitValue = event.submitter.value;
    if (submitValue === "cancel") {
      if (!confirm("プロジェクト作成を取り消しますか？(入力したデータは消去されます)"))event.preventDefault();
    } else {
      // キャンセル以外はそのまま送信
    }
  });
}

const registerButtonEvents = () =>{
  // ボタン要素を取得
  const addButton = document.getElementById("js-add-step");
  
  // ボタンがクリックされた時の処理
  addButton.addEventListener("click", plusStep);
}

const registerStepOperations = () => {
  // ステップの編集用イベント
  document.addEventListener("click", (event) => {
    const target = event.target;
    if (target.className == "" || target.className == undefined) {
      closeElement();
    }
    // 特定の場所をクリックした場合は要素を開く
    if (target.className.indexOf("js-step-operation") != -1) {
      openElement(target.getElementsByTagName("div")[0]);
    }
    // 開いた要素以外をクリックした場合は要素を閉じる
    else {
      closeElement();
    }
  });

  Array.from(document.getElementsByClassName("js-order-up")).forEach(
    (element) => {
      element.addEventListener("click", stepOrderUp);
    }
  );
  Array.from(document.getElementsByClassName("js-step-delete")).forEach(
    (element) => {
      element.addEventListener("click", stepDelete);
    }
  );
};

/**
 * stepに新しいidを付与する
 * isSelectReset=trueでselectの内容(アクション)を新しくする
 */
const setNewId = (element, oldId, newId, isSelectReset = true) => {
  if (element.id === `js-step${oldId}-order`) {
    element.innerHTML = element.innerHTML.replace(String(oldId), String(newId));
  }
  if (element.id === `js-step${oldId}-action-name` && isSelectReset) {
    element.children[0].value = "クリック";
    element.children[0].innerHTML = "クリック";
  }
  if (element.id === `js-step${oldId}-action-str` && isSelectReset) {
    element.setAttribute("disabled", true);
    element.value = "";
    element.setAttribute("placeholder", "-");
  }
  if (element.id === `js-step${oldId}-xpath` && isSelectReset) {
    element.value = "";
  }
  if (element.id != "") {
    element.id = element.id.replace(String(oldId), String(newId));
  }
  if (element.name != "" && element.name != undefined) {
    element.name = element.name.replace(String(oldId), String(newId));
  }

  let childElements = element.children;
  for (let i = 0; i < childElements.length; i++) {
    let childElement = childElements[i];
    setNewId(childElement, oldId, newId, isSelectReset);
  }
};

const plusStep = () => {
  // 複製する要素を取得

  const parent = document.getElementById("js-step-parent");
  const newId = parent.children.length;
  const elementToClone = parent.children[newId - 1 - 1];

  // 要素を複製
  const clonedElement = elementToClone.cloneNode(true);

  setNewId(clonedElement, newId - 1, newId);

  // 親要素の最後から2番目の要素を取得
  const secondLastElement = parent.children[newId - 1];

  // 複製した要素を後ろから2番目に追加
  parent.insertBefore(clonedElement, secondLastElement);

  registerStepOperations();
};

// step右のメニューを開く関数
const openElement = (element) => {
  element.className = "";
  element.id = "js-open-step-operation";
};

// step右のメニューを閉じる関数
const closeElement = () => {
  if (document.getElementById("js-open-step-operation") != undefined) {
    document.getElementById("js-open-step-operation").className = "hidden";
    document.getElementById("js-open-step-operation").id = "";
  }
};

// stepの上移動
const stepOrderUp = (e) => {
  const stepNumUp = Number(e.target.id.split("-")[1].replace("step", ""));
  const parent = document.getElementById("js-step-parent");
  const upStepElement = parent.children[stepNumUp - 1];
  const higherElement = parent.children[stepNumUp - 1 - 1];
  setNewId(higherElement, stepNumUp - 1, Number.MAX_SAFE_INTEGER, false);
  setNewId(upStepElement, stepNumUp, stepNumUp - 1, false);
  setNewId(higherElement, Number.MAX_SAFE_INTEGER, stepNumUp, false);
  parent.insertBefore(upStepElement, higherElement);
};

// step削除 
const stepDelete = (e) => {
  const stepCount = getStepCount();
  if(stepCount <= 1){
    return;
  }

  const parent = document.getElementById("js-step-parent");
  const deleteStepNum = Number(e.target.id.split("-")[1].replace("step", ""));

  // 要素削除
  const target = parent.children[deleteStepNum - 1];
  target.remove();

  // 最大値まで1個ずつidを若くする
  for (let i = deleteStepNum; i <= stepCount; i++) {
    const shiftElement = parent.children[i - 1];
    setNewId(shiftElement, i + 1, i, false);
  }
};

// Selectの文字入力が選ばれた時用の処理
const handleSelectChange = (e) => {
  if (e.target.value === "文字入力" || e.target.value === "文字入力後Enter") {
    e.target.parentNode
      .getElementsByTagName("input")[0]
      .removeAttribute("disabled");
    e.target.parentNode
      .getElementsByTagName("input")[0]
      .setAttribute("placeholder", "使用する文字を入力");
    e.target.parentNode.getElementsByTagName("input")[0].focus();
  } else {
    e.target.parentNode.getElementsByTagName("input")[0].value = "";
    e.target.parentNode
      .getElementsByTagName("input")[0]
      .setAttribute("disabled", true);
    e.target.parentNode
      .getElementsByTagName("input")[0]
      .setAttribute("placeholder", "-");
  }
};

