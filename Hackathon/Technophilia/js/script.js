document.querySelector("#recurrance4").innerHTML = "checking"
document.querySelector("#eventtype1").onclick = function() {  
    document.querySelector("#eventstarttime").value = '00:00';
    document.querySelector("#eventendtime").value = '23:59';
    $("#eventstarttime").prop('readonly', true);
    $("#eventendtime").prop('readonly', true);
    document.querySelectorAll(".timeset")[0].style.display = '';
    document.querySelectorAll(".timeset")[1].style.display = '';
}


document.querySelector("#eventtype2").onclick = function() {  
document.querySelector("#eventstarttime").value = '';
document.querySelector("#eventendtime").value = '';
$("#eventstarttime").prop('readonly', false);
$("#eventendtime").prop('readonly', false);
document.querySelectorAll(".timeset")[0].style.display = '';
document.querySelectorAll(".timeset")[1].style.display = '';
}

document.querySelector("#myform").addEventListener("submit",
function(event){
    console.log("here")
    event.preventDefault();
    handleForm(this)
}, true)

function handleForm(form){

    var missing = false
    var compulsory = ['eventname','eventimp','eventdate','eventype','eventstarttime','eventendtime','desc','recurrance','eventpurpose']
    for (i=0;i<compulsory.length;i++) {
        if (form[compulsory[i]].value == '') {
            console.log("missing parameters but defined!!" + compulsory[i]);
            missing = true
            console.log(missing)
        }
    }
    const d = new Date();
    currentdate = d.getDate();
    currentmonth = d.getMonth();
    currentmonth = currentmonth + 1;
    currentyear = d.getFullYear();
    inputdate = form['eventdate'].value.split("-")[2];
    inputmonth = form['eventdate'].value.split("-")[1];
    inputyear = form['eventdate'].value.split("-")[0];
    currenthour = d.getHours();
    inputhour = form['eventstarttime'].value.split(":")[0]
    if (missing==true) {
        console.log("reached here")
        console.log(currenthour);
        console.log(inputhour);
        document.querySelector(".alertmsg").style.display = ""
        document.querySelector(".alertmsg").innerHTML = "Please fill all necessary inputs before submitting"

    }
    else if (inputyear < currentyear || (currentyear==inputyear && inputmonth < currentmonth) || (currentyear==inputyear && inputmonth == currentmonth && inputdate < currentdate)) {
        console.log("invalid date")
        document.querySelector(".alertmsg").style.display = ""
        document.querySelector(".alertmsg").innerHTML = "Invalid Date"
    }
    else if (currentyear==inputyear && inputmonth == currentmonth && inputdate == currentdate && inputhour <= currenthour) {
        document.querySelector(".alertmsg").style.display = ""
        document.querySelector(".alertmsg").innerHTML = "Please select a Start Time atleast one hour from now"
    }
    else {
        console.log("SUccesss!!!")
        google.script.run.hello(form);
        location.replace("https://www.google.com/")
    }
}