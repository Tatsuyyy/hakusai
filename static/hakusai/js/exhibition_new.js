window.onload = () => {
  registerButtonEvents();
  registerExhibitionOperations();
};

const getExhibitionCount = () => {
  const parent = document.getElementById("js-exhibition-parent");
  return parent.children.length - 1;
};

const registerButtonEvents = () => {
  // ボタン要素を取得
  const addButton = document.getElementById("js-add-exhibition");

  // ボタンがクリックされた時の処理
  addButton.addEventListener("click", plusExhibition);
};

const registerExhibitionOperations = () => {
  // 展示設定の編集用イベント
  document.addEventListener("click", (event) => {
    const target = event.target;
    if (target.className == "" || target.className == undefined) {
      closeElement();
    }
    // 特定の場所をクリックした場合は要素を開く
    if (target.className.indexOf("js-exhibition-operation") != -1) {
      openElement(target.getElementsByTagName("div")[0]);
    }
    // 開いた要素以外をクリックした場合は要素を閉じる
    else {
      closeElement();
    }
  });

  Array.from(document.getElementsByClassName("js-order-up")).forEach(
    (element) => {
      element.addEventListener("click", exhibitionOrderUp);
    }
  );
  Array.from(document.getElementsByClassName("js-exhibition-delete")).forEach(
    (element) => {
      element.addEventListener("click", exhibitionDelete);
    }
  );
};

/**
 * 展示設定に新しいidを付与する
 * isReset=trueでformの内容を新しくする
 */
const setNewId = (element, oldId, newId, isReset=true) => {
  if (element.id === `js-exhibition${oldId}-order`) {
    element.innerHTML = element.innerHTML.replace(String(oldId), String(newId));
  }
  if (element.id === `js-exhibition${oldId}-project-name`) {
    element.children[0].selectIndex=0
  }
  if (element.id === `js-exhibition${oldId}-repeat` && isReset) {
    element.value = 1;
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
    setNewId(childElement, oldId, newId, isReset);
  }
};

const plusExhibition = () => {
  // 複製する要素を取得

  const parent = document.getElementById("js-exhibition-parent");
  const newId = parent.children.length;
  const elementToClone = parent.children[newId - 1 - 1];

  // 要素を複製
  const clonedElement = elementToClone.cloneNode(true);

  setNewId(clonedElement, newId - 1, newId, true);

  // 親要素の最後から2番目の要素を取得
  const secondLastElement = parent.children[newId - 1];

  // 複製した要素を後ろから2番目に追加
  parent.insertBefore(clonedElement, secondLastElement);

  registerExhibitionOperations();
};

// 展示設定の右のメニューを開く関数
const openElement = (element) => {
  element.className = "";
  element.id = "js-open-exhibition-operation";
};

// 展示設定の右のメニューを閉じる関数
const closeElement = () => {
  if (document.getElementById("js-open-exhibition-operation") != undefined) {
    document.getElementById("js-open-exhibition-operation").className =
      "hidden";
    document.getElementById("js-open-exhibition-operation").id = "";
  }
};

// 展示設定の上移動
const exhibitionOrderUp = (e) => {
  const exhibitionNumUp = Number(
    e.target.id.split("-")[1].replace("exhibition", "")
  );
  const parent = document.getElementById("js-exhibition-parent");
  const upExhibitionElement = parent.children[exhibitionNumUp - 1];
  const higherElement = parent.children[exhibitionNumUp - 1 - 1];
  setNewId(higherElement, exhibitionNumUp - 1, Number.MAX_SAFE_INTEGER, false);
  setNewId(upExhibitionElement, exhibitionNumUp, exhibitionNumUp - 1, false);
  setNewId(higherElement, Number.MAX_SAFE_INTEGER, exhibitionNumUp, false);
  parent.insertBefore(upExhibitionElement, higherElement);
};

// 展示設定削除
const exhibitionDelete = (e) => {
  const exhibitionCount = getExhibitionCount();
  if(exhibitionCount <= 1){
    return;
  }

  const parent = document.getElementById("js-exhibition-parent");
  const deleteExhibitionNum = Number(
    e.target.id.split("-")[1].replace("exhibition", "")
  );

  // 要素削除
  const target = parent.children[deleteExhibitionNum - 1];
  target.remove();

  // 最大値まで1個ずつidを若くする
  for (let i = deleteExhibitionNum; i <= exhibitionCount; i++) {
    const shiftElement = parent.children[i - 1];
    setNewId(shiftElement, i + 1, i, false);
  }
};