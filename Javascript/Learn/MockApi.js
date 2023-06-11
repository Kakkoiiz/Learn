var courseApi = 'http://localhost:3000/courses';

fetch(courseApi)
  .then(function(response) {
    return response.json();
  })
  .then(function(courses) {
    var postBlock = document.getElementById('post-block');
    var html = '';

    courses.forEach(function(course) {
      html += `<li>
        <h2>${course.id}</h2>
        <h2>${course.name}</h2>
        <h2>${course.description}</h2>
        <img src="${course.img}" alt="${course.name}" class="img">
      </li>`;
    });

    postBlock.innerHTML = html;
  });