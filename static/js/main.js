$( document ).ready(function() {
    $.ajax({
        url: '/solve_get_json',
        data: 'board='+$('#boardInput').val(),
        type: 'GET',
        dataType: 'json',
        success: function(response) {
            numWordsText = 'Num words in solution: ' + response.solution.num_words;
            $('#numWordsInSolution').html(numWordsText);
            words = response.solution.words.join(' ');
            $('#wordsInSolution').html(words);
            $('#solutionToggleButton').text('Show Solution').removeAttr('disabled');
        },
        error: function(error) {
            console.log(error)
        }
    });


    $('[data-toggle="collapse"]').click(function() {
        if ($(this).attr('aria-expanded')) {
            $(this).text("Hide Solution");
        } else {
            $(this).text("Show Solution");
        }
    });

});
