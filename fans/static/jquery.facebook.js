var facebook = {
    apiKey: ""
    
    
}


var api_key = 'dda2adcf9ab358e7fe0457db6be8318b';
var channel_path = '/static/xd_receiver.htm';
FB_RequireFeatures(["Api"], function(){
    // Create an ApiClient object, passing app's API key and 
    // a site relative URL to xd_receiver.htm
    FB.Facebook.init(api_key, channel_path);

    var api = FB.Facebook.apiClient;
    // require user to login 
    api.requireLogin(function(exception){
        FB.FBDebug.logLevel=1;
        FB.FBDebug.dump("Current user id is " + api.get_session().uid);


		
        // Get friends list 

       //5-14-09: this code below is broken, correct code follows 
       //api.friends_get(null, function(result){
       //     Debug.dump(result, 'friendsResult from non-batch execution ');
       // });

         api.friends_get(new Array(), function(result, exception){
              FB.FBDebug.dump(result, 'friendsResult from non-batch execution ');
         });
    });
});