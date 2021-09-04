/* JQuery for Materialize */

$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.tooltipped').tooltip();
  });

// Code from https://github.com/Henriqueperoni/CI-MS3-Books-World/blob/master/static/js/script.js
  // Add book modal
function startModalBooks() {
  const modal = document.querySelector(".container-modal")
  modal.classList.add("show-modal");

  modal.addEventListener("click", (e) => {
      if (e.target.id == "modal-review" || e.target.className == "close-modal") {
          modal.classList.remove("show-modal")
      }
  })
}

// Event Listener that starts the add book modal
document.addEventListener('DOMContentLoaded', function () {
  const addBook = document.getElementById("add-book")
  if (addBook) {
      addBook.addEventListener("click", () => {
          startModalBooks()
      })
  }
})

// Event Listener that starts the edit book modal
document.addEventListener('DOMContentLoaded', function () {
  const editBook = document.getElementById("edit-book")
  if (editBook) {
      editBook.addEventListener("click", () => {
          startModalBooks()
      })
  }
})

// Delete Modal
function deleteModal() {
  const modal = document.querySelector(".container-modal-delete")
  modal.classList.add("show-modal-delete");

  modal.addEventListener("click", (e) => {
      if (e.target.id == "modal-delete" || e.target.className == "close-modal-delete" || e.target.id == "cancel-delete") {
          modal.classList.remove("show-modal-delete")
      }
  })
}

// Event Listener that starts delete modal
document.addEventListener('DOMContentLoaded', function () {
  const deleteBook = document.getElementById("delete-book")
  if (deleteBook) {
      deleteBook.addEventListener("click", () => {
          deleteModal()
      })
  }
})

// Add list modal
function startModalEditList() {
  const modal = document.querySelector(".container-modal-list")
  modal.classList.add("show-modal");

  modal.addEventListener("click", (e) => {
      if (e.target.id == "modal-edit-list" || e.target.className == "close-modal") {
          modal.classList.remove("show-modal")
      }
  })
}

// Event listener that starts add list modal
document.addEventListener('DOMContentLoaded', function () {
  const editList = document.getElementById("edit-list")
  if (editList) {
      editList.addEventListener("click", () => {
          startModalEditList()
      })
  }
})

// Function to dynamically add input fields
//https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery
$(document).ready(function () {
  let maxFields = 3; //maximum input boxes allowed
  let addButton = $(".add-field-button"); //Add button ID
  let inputs = $(".container-inputs")

  let x = 1; //initlal text box count
  $(addButton).click(function (e) { //on add input button click
      console.log('clicked')
      e.preventDefault();
      if (x < maxFields) { //max input box allowed
          x++; //text box increment
          $(inputs).append('<div class="input-field col s12 add-vendor"><label for="vendor_url">Vendor URL:</label><input id="vendor_url" name="vendor_url" type="text" class="validate" minlength="5" maxlength="100" required><a href="#" class="remove_field btn-small red darken-2">Remove</a></div>'); //add input box
      }
  });

  $(inputs).on("click", ".remove_field", function (e) { //user click on remove text
      e.preventDefault(); $(this).parent('div').remove(); x--;
  })
});

// Add Active Navigation Class Based on URL
// https://css-tricks.com/snippets/jquery/add-active-navigation-class-based-on-url/
$(function () {
  $('nav a[href^="/' + location.pathname.split("/")[1] + '"]').addClass('active');
});