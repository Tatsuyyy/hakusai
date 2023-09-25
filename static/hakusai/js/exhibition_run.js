window.onload = () => {
    registerButtonEvents();
};




const registerButtonEvents = () => {
    const startButton = document.getElementById("js-start-button");
    const stopButton = document.getElementById("js-stop-button");
    const statusText = document.getElementById("js-exhibition-status");

    const getCookie = (name) => {
      if (document.cookie && document.cookie !== "") {
        for (const cookie of document.cookie.split(";")) {
          const [key, value] = cookie.trim().split("=");
          if (key === name) {
            return decodeURIComponent(value);
          }
        }
      }
    };
   
    const fetchApi = async (operation) => {
        const csrftoken = getCookie("csrftoken");
        return fetch(endPoint, {
          method: "POST",
          body: JSON.stringify({
            "operation": operation,
          }),
          headers: {
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "X-CSRFToken": csrftoken,
          },
        }).then(async (response) => {
          return await response.json();
        });
    };

    startButton.addEventListener("click", async () => {
        const res = await fetchApi(operation='start');
        console.log(res);
        stopButton.removeAttribute("disabled");
        startButton.children[0].classList.replace("text-green-500", "text-gray-400");
        startButton.children[1].classList.replace("text-gray-700", "text-gray-400");
        stopButton.children[0].classList.replace("text-gray-400", "text-red-600");
        stopButton.children[1].classList.replace("text-gray-400", "text-gray-700");
        statusText.innerText = "を再生中...";
        startButton.setAttribute("disabled", true);
    });

    stopButton.addEventListener("click", async () => {
        const res = await fetchApi(operation='stop');
        console.log(res);
        startButton.removeAttribute("disabled");
        stopButton.children[0].classList.replace("text-red-600", "text-gray-400");
        stopButton.children[1].classList.replace("text-gray-700", "text-gray-400");
        startButton.children[0].classList.replace("text-gray-400", "text-green-500");
        startButton.children[1].classList.replace("text-gray-400", "text-gray-700");
        statusText.innerText = "を停止中";
        stopButton.setAttribute("disabled", true);
    });

    stopButton.children[0].classList.replace("text-red-600", "text-gray-400");

};
