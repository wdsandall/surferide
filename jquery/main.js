var url = 'http://magicseaweed.com/api/46b2f2f1d095df7f57d4d3a080731311/forecast/?spot_id=1&fields=solidRating,fadedRating'

$.ajax({
    dataType: "jsonp",
    url: url
}).done(function(data) {
    console.log(data);
    // The result is an array, so loop over each one
    $.each(data, function() {
        $("#test").append(this.solidRating + "   ");

        $("#test2").append(this.fadedRating + "   ");
    });
});
