//add value fail
var creditH = [];
var letterG = [];


var $ = function (id) {
    return document.getElementById(id);
};

var add = function () {
    //Add credit_hour
    var credit_hour = parseInt($("credit_hour").value);
    
    if (isNaN(credit_hour) || credit_hour < 0) {
    	alert("The credit hour must be a number and bigger than 0!");
    }
    else {
        creditH[creditH.length] = credit_hour;
    }

    //Add letter_grade
    var letter_grade = $("letter_grade").value;
    letter_grade = letter_grade.toUpperCase();
    
    if(letter_grade === 'A'){
        letter_grade = 4.0;
    }
    else if(letter_grade === 'B'){
        letter_grade = 3.0;
    }
    else if (letter_grade === 'C'){
        letter_grade = 2.0;
    }
    else if (letter_grade === 'D'){
        letter_grade = 1.0;
    }
    else if (letter_grade === 'F'){
        letter_grade = 0; 
    }
    letterG[letterG.length] = letter_grade.toFixed(1);
    
    //display the result
    $("display").value="";
    for(var i = 0; i < letterG.length; i++)
        {
         $("display").value += "Credit Hour: " + creditH[i] + "  GPA: " + letterG[i] + "\n";   
        }
    $("credit_hour").value = "";
    $("letter_grade").value = "";
}

var calculate = function () {
    var totalT = 0;
    var totalD = 0;
    var averageGPA = 0;
    if(letterG.length < 2)
        {
            alert("Please add another course. The calculator needs at least two courses to calculate!");
        }
    else{
        //calculate the top part of the equation
        //And the bottom part of the equation
        for(var i = 0; i < letterG.length; i++)
            {
                totalT += letterG[i]*creditH[i];
                totalD += creditH[i];
            }
        //calculation
        averageGPA = (totalT/totalD).toFixed(3);
        
        $("display").value = "";
        $("display").value = " The average GPA is: " + averageGPA; 
    }
}

//$("display").value = letter_grade;
window.onload = function () {
    $("add").onclick = add;
    $("calculate").onclick = calculate;
}