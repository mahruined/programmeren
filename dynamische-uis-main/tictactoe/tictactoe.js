const PLAYER_ONE = 'X'
const PLAYER_TWO = 'O'
const winning_condition = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6],
]
const cellElemenets = document.querySelectorAll('[data-cell]')
const boardElements = document.getElementById('board')
const winningMessageElement = document.getElementById('winningmessage')
const restartbutton = document.getElementById('restartbutton')
const winningmessageTextelement = getElementById('winningmessagetext')
let PLAYER_TWO_Turn = false


startgame()
restartbutton.addEventListener('click',startgame)
function startgame(){
    PLAYER_TWO_Turn = false
    cellElemenets.foreach(cell =>{
        cell.classlist.remove(PLAYER_ONE)
        cellclasslist.remove(PLAYER_TWO)
        cell.removeEventlistener('click', HandleCellClick)
        celladd.addEventListener('click', HandleCellClick,{once: True})

    })
    setboardhoverclass()
    winningMessageElement.classList.remove('show')
}   
function HandleCellClick(e){
    const cell = e.target
    const currentClass = PLAYER_TWO_Turn ? player
}