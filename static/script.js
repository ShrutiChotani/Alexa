window.onload = function() {
    // Wait for the intro animation to finish
    setTimeout(function() {
        var introContainer = document.getElementById('intro-container');
        introContainer.style.opacity = '0'; // Set opacity to 0 to fade out
        introContainer.style.pointerEvents = 'none'; // Disable pointer events during animation

        // Hide the intro container after animation completes
        setTimeout(function() {
            introContainer.style.display = 'none';
        }, 40000); // Adjust the time to match the animation duration
    }, 40000); // Adjust the time to match the animation duration
};

function runPythonScript(){
    // send a request to flask server
    fetch("/run_script")
    .then(response => response.json())
    .then(data =>{
        console.log(data);
        const outputDiv=document.getElementById("output");
        if (data.responses) {
            // Use map function only if data.responses is defined
            outputDiv.innerHTML = data.responses.map(response => `<p>${response}</p>`).join('');
        } else {
            outputDiv.innerHTML = "<p>No responses received.</p>";
        }
    })
    .catch(error => console.error(error));
}


function showMicIcon(){
    const micIcon=document.getElementById('mic-icon');
    micIcon.style.opacity='1';
}
function hideMicIcon(){
    const micIcon=document.getElementById('mic-icon');
    micIcon.style.opacity='0';
}
function runAlexa(){
    responses=[];
    showMicIcon;
    while(true){
        command=takeCommand();

        if('bye'in command){
            hideMicIcon();
        }
    }
}
window.onload = function () {
    showMicIcon();
};



const cursor=document.querySelector(".cursor");
var timeout;

document.addEventListener('mousemove', (e)=>{
    let x=e.pageX;
    let y=e.pageY;
    cursor.style.top=y+"px";
    cursor.style.left=x+"px";
    cursor.style.display='block';
    function mouseStopped(){
        cursor.style.display="none";
    }
    clearTimeout(timeout);
    timeout=setTimeout(mouseStopped,1000);
});

document.addEventListener('mouseenter', () => {
    cursor.style.display = 'block';
});

document.addEventListener('mouseleave', () => {
    cursor.style.display = 'none';
});