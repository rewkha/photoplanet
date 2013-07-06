/**
 * Created with PyCharm.
 * User: rewkha
 * Date: 06.07.13
 * Time: 02:58
 * To change this template use File | Settings | File Templates.
 */


$(document).ready(function(){
    $('.js-vote').on('click', function(){
        var photo_id = $(this).attr('data-id');
        var vote = $(this).attr('data-vote');
        self = this;
        console.log($(this).find('span'));
        $.ajax({
            url: window.vote_url,
            data: {'photo': photo_id, 'vote': vote},
            type: 'POST',
            success: function(data){
                $(self).parent().find('span').text(data.votes);
            }

        });
        return false;
    })

})