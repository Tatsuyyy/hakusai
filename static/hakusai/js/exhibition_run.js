window.onload = () => {
    registerButtonEvents();
};

const registerButtonEvents = () => {
    const startButton = document.getElementById("js-start-button");
    const stopButton = document.getElementById("js-stop-button");
    const statusText = document.getElementById("js-exhibition-status");

    startButton.addEventListener("click", () => {
        stopButton.removeAttribute("disabled");
        startButton.children[0].classList.replace("text-green-500", "text-gray-400");
        startButton.children[1].classList.replace("text-gray-700", "text-gray-400");
        stopButton.children[0].classList.replace("text-gray-400", "text-red-600");
        stopButton.children[1].classList.replace("text-gray-400", "text-gray-700");
        statusText.innerText = "を再生中...";
        startButton.setAttribute("disabled", true);
    });

    stopButton.addEventListener("click", () => {
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
