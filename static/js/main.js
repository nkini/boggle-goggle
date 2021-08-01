function get_and_populate_solution(board_input) {
    $.ajax({
        url: '/solve_get_json',
        data: 'board='+board_input,
        type: 'GET',
        dataType: 'json',
        success: function(response) {
            // Num of words text
            numWordsText = 'Num words in solution: ' + response.solution.num_words;
            $('#numWordsInSolution').html(numWordsText);
            // Actual solution box
            words = get_words_sorted_by_length(response.solution.words)
            $('#wordsInSolution').html(words);
            // Hide / Show Solution button
            $('#solutionToggleButton').text('Show Solution').removeAttr('disabled');
        },
        error: function(error) {
            console.log(error)
        }
    });
}

function get_words_sorted_by_length(solution_words) {
    if (solution_words.length == 0) {
        return ''
    }
    solution_words.sort((a, b) => (b.length - a.length) || a.localeCompare(b));
    words_in_solution_html = ''
    same_length_words_string = ''
    prev_word_length = solution_words[0].length
    $.each(solution_words, function( index, value ) {
        if (value.length != prev_word_length) {
            words_in_solution_html += '<p>' + same_length_words_string + '</p>'
            prev_word_length = value.length
            same_length_words_string = ''
        }
        same_length_words_string += value + ' '
    });
    words_in_solution_html += '<p>' + same_length_words_string + '</p>'
    return words_in_solution_html
}

$('[data-toggle="collapse"]').click(function() {
    if ($(this).attr('aria-expanded') == "false") {
        $(this).text("Hide Solution");
    } else {
        $(this).text("Show Solution");
    }
});
