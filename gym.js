// This section of javascript is the validation used on the contact form on the contact.html page, it will check for empty values on some fields and check others to ensure number e.g. Zip is NaN or empty - will it will focus back in that field and request correct information. 

//Once all fields are populated correctly using the validation below a pop up will advise - "Submitted". You then have the option to reset the form or navigate to another page.

      function validate() {
      
         if( document.myForm.Name.value == "" ) {
            alert( "Please provide your Name!" );
            document.myForm.Name.focus() ;
            return false;
         }
         if( document.myForm.EMail.value == "" ) {
            alert( "Please provide your Email!" );
            document.myForm.EMail.focus() ;
            return false;
         }
           
         if( document.myForm.County.value == "-1" ) {
            alert( "Please provide your county!" );
            return false;
         }
		 
		  if( document.myForm.question.value == "" ) {
            alert( "Please ask your Question!" );
            document.myForm.Name.focus() ;
            return false;
         }
		 
         return( true );
		 
	  }
