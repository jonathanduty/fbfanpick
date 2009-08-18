(function(){
    
    var searchURL = "http://api.yelp.com/business_review_search?term="
    
    jQuery.fn.yelpSearch = function(api_key,inputField,resultDiv) {
        
        alert("setting up");
        var self = this;
        
        
        $(self).each(function(element) {
            $(element).keyup(function() {
                alert(inputField.attr("value"));
            });
        });
        
    }
    
})();        