// //dice roll number generator
// //abe, tony and bradley
// var iRollDice;
// var i;
// iRollDice = prompt("How many times we want to roll the dice?",5);
// for (i=1; i<=iRollDice; i++){
// 	//this asks the user how many times should the dice roll.
// iRandomNumber = Math.ceil(Math.random()*6);
// //it spits numbers between 1 and six
// document.writeln(iRandomNumber+"<br>");  
// console.log(`The dice roll is ${iRandomNumber}`)
// //this displays the numbers from top to bottom instead of a straight line
// }
// document.writeln("----- Finished -----");  //this message pops at the end


const roll = () => Math.random() * (6 - 1) + 1;

module.exports = {
	roll
};