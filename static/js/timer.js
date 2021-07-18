$('#timer-display').html('3:00');
var timer = null;

function setTime() {
    var displayedTime = $('#timer-display').html().split(':');
    if (displayedTime[0] == '0' && displayedTime[1] == '00') {
        clearInterval(timer);
        return;
    }
    var minutes = parseInt(displayedTime[0], 10);
    var seconds = parseInt(displayedTime[1], 10);
    if (--seconds < 0) {
        minutes--;
        seconds = 59;
    }
    seconds = (seconds < 10) ? '0' + seconds : seconds;
    $('#timer-display').html(minutes + ':' + seconds);
}

$('#timer-starter').click(function() {
    if (!timer) {
        timer = setInterval(setTime, 1000);
    }
});

function stopTimer() {
    if (timer) {
        clearInterval(timer);
        timer = null;
    }
}

$('#timer-stopper').click(stopTimer);

$('#timer-resetter').click(function() {
    stopTimer();
    $('#timer-display').html('3:00');
});
