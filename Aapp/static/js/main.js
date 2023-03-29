// prompt('sdfsdf');
function like(id) {
  // alert(id);
  fetch("/like/"+id)
    .then(response => response.json())
    .then(data => {
      const likes = document.getElementById('data_'+id);
      // alert(id);
      likes.innerText = data.rating;
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

document.addEventListener("DOMContentLoaded", () => {
  const likeButtons = document.querySelectorAll(".like-button");
  likeButtons.forEach(button => {
    button.addEventListener("click", () => {
      const id = button.dataset.id;
      // alert(id);
      like(id);
    });
  });
});


function dislike(id) {
  // alert(id);
  fetch("/dislike/"+id)
    .then(response => response.json())
    .then(data => {
      const dislikes = document.getElementById('data_'+id);
      // alert(id);
      dislikes.innerText = data.rating;
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

document.addEventListener("DOMContentLoaded", () => {
  const dislikeButtons = document.querySelectorAll(".dislike-button");
  dislikeButtons.forEach(button => {
    button.addEventListener("click", () => {
      const id = button.dataset.id;
      // alert(id);
      dislike(id);
    });
  });
});
