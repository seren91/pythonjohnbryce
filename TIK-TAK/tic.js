const winner = document.getElementById("winner");
const cells = document.querySelectorAll(".cell");
const restartButton = document.getElementById("restart-button");
//const turnInfo = document.getElementById("turn-info");


const players = {
    x: "x",
    o: "o",
}
let currentPlayer = "";
let isGameRunning = false;
let boardState = Array(9).fill("");
const winLines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [2, 4, 6],
    [0, 4, 8],
];

window.addEventListener("load", () => {
    initializeGame();
    startGame();
});
function initializeGame() {
    cells.forEach(cell => {
        cell.addEventListener("click", clickCell);
    });
    restartButton.addEventListener("click", restartGame);
}


function startGame() {
    isGameRunning = true;
    cells.forEach(cell => cell.textContent = "");
    winner.textContent = "";
    currentPlayer = players.x;
    
}


function clickCell() {
    if(!isGameRunning) {
        return;
    }
    if(this.textContent) {
        return;
    }
    this.textContent = currentPlayer;
    const cellIndex = this.dataset.cellIndex;
    boardState[cellIndex] = currentPlayer;
    if(checkGameOver()) {
        return finishGame();
    }
    currentPlayer = (currentPlayer === players.x) ? players.o : players.x;
    
}

function finishGame() {
    isGameRunning = false;
    boardState = Array(9).fill("");      
    
    

}

function checkLine(line) {
    const [a, b, c] = line;

    const cellA = boardState[a];
    const cellB = boardState[b];
    const cellC = boardState[c];

    if([cellA, cellB, cellC].includes("")) {
        return false;
    }
    return cellA === cellB && cellB === cellC;
}


function checkGameOver() {
    for(const line of winLines) {
        if(checkLine(line)) {
            winner.textContent = `${currentPlayer} Win !!!`;
            finishGame();
            
            return false;
        }
        
    }
    if(!boardState.includes("")) {
        winner.textContent = "Draw!!!!!";
        finishGame();
            
        return false;
        
    }
}

function restartGame() {
    finishGame();
    startGame();
}
