document.querySelector("#eventtype1").onclick = function() {  
    document.querySelector("#eventstarttime").value = '00:00';
    document.querySelector("#eventendtime").value = '23:59';
    $("#eventstarttime").prop('readonly', true);
    $("#eventendtime").prop('readonly', true);
    document.querySelector(".timeset1").style.display = 'block';
    document.querySelector(".timeset2").style.display = 'block';
}


document.querySelector("#eventtype2").onclick = function() {  
    document.querySelector("#eventstarttime").value = '';
    document.querySelector("#eventendtime").value = '';
    $("#eventstarttime").prop('readonly', false);
    $("#eventendtime").prop('readonly', false);
    document.querySelector(".timeset1").style.display = 'block';
    document.querySelector(".timeset2").style.display = 'block';
}

document.querySelector("#myform").addEventListener("submit",
    function(event){
        //console.log("here")
        event.preventDefault();
        handleForm(this)
}, true)

function disableButton(button) {
    //console.log("tporuwpeoriwep")
    document.querySelector(button).disabled = true;
    //console.log("yooo")
    document.querySelector(button).style["background-color"] = "#D3D3D3";
    //console.log("pwoli")
    document.querySelector(button).style["color"] = "#EBECF0";
}

function getClasses() {
    classlist = document.querySelectorAll(".eventclass");
    selectedClasses = []
    for (const classcheckbox in classlist) {
        if (classcheckbox.checked) {
            selectedClasses.push(classcheckbox.value)
        }
    }
}

function getStudents (selectedClasses) {
    var gueststudents = []
    for (const guestclass in selectedClasses) {
        $ajaxUtils.sendGetRequest("data/students.json", 
        function(students){
            gueststudents = gueststudents.concat(students[guestclass])
        });
    }
    return guesttudents
}

function handleForm(form){

    var missing = false
    var compulsory = ['eventname','eventimp','eventdate','eventtype','eventstarttime','eventendtime','desc','recurrance','eventpurpose']
    for (i=0;i<compulsory.length;i++) {
        if (form[compulsory[i]].value == '') {
            //console.log("missing parameters but defined!!" + compulsory[i]);
            missing = true
            //console.log(missing)
        }
    }

    var d = new Date();
    currentdate = d.getDate();
    currentmonth = d.getMonth();
    currentmonth = currentmonth + 1;
    currentyear = d.getFullYear();
    inputdate = form['eventdate'].value.split("-")[2];
    inputmonth = form['eventdate'].value.split("-")[1];
    inputyear = form['eventdate'].value.split("-")[0];
    currenthour = d.getHours();
    currentmin = d.getMinutes();
    inputstarthour = form['eventstarttime'].value.split(":")[0]
    inputendhour = form['eventendtime'].value.split(":")[0]
    inputstartmin = form['eventstarttime'].value.split(":")[1]
    inputendmin = form['eventendtime'].value.split(":")[1]
    eventtype = form["eventtype"].value;

    if (missing==true) {
        //console.log("reached here")
        ////console.log(currenthour);
        ////console.log(inputstarthour);
        document.querySelector(".alertmsg").style.display = "block"
        document.querySelector(".alertmsg").innerHTML = "Please fill all necessary inputs before submitting"
    }
    else if (inputyear < currentyear || (currentyear==inputyear && inputmonth < currentmonth) || (currentyear==inputyear && inputmonth == currentmonth && inputdate < currentdate)) {
        //console.log("invalid date")
        document.querySelector(".alertmsg").style.display = "block"
        document.querySelector(".alertmsg").innerHTML = "Invalid Date"
    }
    else if (currentyear==inputyear && inputmonth == currentmonth && inputdate == currentdate && (inputstarthour < currenthour ||  (inputstarthour==currenthour && inputstartmin < (currentmin + 10))) && eventtype == "Time Based") {
        document.querySelector(".alertmsg").style.display = "block"
        document.querySelector(".alertmsg").innerHTML = "Please select a Start Time atleast 10 minutes from now"
        ////console.log("here now")
    }
    else if (inputendhour < inputstarthour || (inputendhour == inputstarthour && inputendmin <= inputstartmin)) {
        document.querySelector(".alertmsg").style.display = "block"
        document.querySelector(".alertmsg").innerHTML = "Invalid End Time"
        ////console.log("here now 2")
    }
    else {
        //console.log("SUccesss!!!")
        google.script.run.createEvent(form);
        //location.replace("https://www.google.com")
        disableButton("#submit");
    }
}
