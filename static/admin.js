ClassicEditor
			.create( document.querySelector( '.editor' ), {

				toolbar: {
					items: [
						'heading',
						'|',
						'bold',
						'italic',
						'link',
						'bulletedList',
						'numberedList',
						'codeBlock',
						'|',
						'indent',
						'outdent',
						'|',
						'imageUpload',
						'blockQuote',
						'insertTable',
						'undo',
						'redo'
					]
				},
				language: 'en',
				image: {
					toolbar: [
						'imageTextAlternative',
						'imageStyle:full',
						'imageStyle:side'
					]
				},
				table: {
					contentToolbar: [
						'tableColumn',
						'tableRow',
						'mergeTableCells'
					]
				},
				licenseKey: '',

			} )
			.then( editor => {
				window.editor = editor;








			} )
			.catch( error => {
				console.error( 'Oops, something went wrong!' );
				console.error( 'Please, report the following error on https://github.com/ckeditor/ckeditor5/issues with the build id and the error stack trace:' );
				console.warn( 'Build id: nqi6ql2n5tsm-2twh7gw74a3e' );
				console.error( error );
			} );

  // Your web app's Firebase configuration
  var firebaseConfig = {
    apiKey: "AIzaSyC7WumGICm0aAv9eKGFuw_rzzNlyrgYGSw",
    authDomain: "app1-ffc93.firebaseapp.com",
    databaseURL: "https://app1-ffc93.firebaseio.com",
    projectId: "app1-ffc93",
    storageBucket: "app1-ffc93.appspot.com",
    messagingSenderId: "124680641386",
    appId: "1:124680641386:web:f611cf33a5efb83b56e313"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);



function data() {
    var link = document.getElementById("link").value;
    var title = document.getElementById("title").value;
    var subtitle = document.getElementById("subtitle").value;
    var img = document.getElementById("img").value;
    if (link == "" || title == "" || subtitle == "" || img == "") {
		alert("You Must Fill in all the things! ");
		return null;
	}
    firebase.database().ref('link/' + link).set({
        "content": `${editor.getData()}`
      });
	firebase.database().ref().child('home').push({
        "title": `${title}`,
		"subtitle": `${subtitle}`,
		"img": `${img}`,
		"link": `${link}`
      });
	  document.getElementById("link").value = ""
	  document.getElementById("title").value = ""
	  document.getElementById("subtitle").value = ""
	  document.getElementById("img").value = ""
	  editor.setData("");
    }