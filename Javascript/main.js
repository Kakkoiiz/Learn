



var courseApi = 'http://localhost:3000/courses';


function start() {
  getCourses(renderCourses);

  handleCreateFrom();

};


start();


function getCourses(callback) {
  fetch(courseApi)
    .then(function(response) {
      return response.json()
    })
    .then(callback)
};


function createCourse(data, callback) {
  var options = {
    method: 'POST',
    headers: {
      'Content-type': 'application/json'
    },
    body: JSON.stringify(data)

  };
  fetch(courseApi, options)
    .then(function(response){
      return response.json();
    })
    .then(callback);
}



function renderCourses(courses) {
  var listCoursesBlock = document.querySelector('#list-courses');
  var htmls = courses.map(function(course) {
    return `
      <li class="course-item-${course.id}"> 
        <h4>${course.name}</h4>
        <p>${course.description}</p>
        <button onclick="handleDeleteCourse(${course.id})">Xóa</button>
        <button onlick ="showUpdate()">Cap nhat</button>
      </li>
    `
  })
  listCoursesBlock.innerHTML = htmls.join('')
}


function handleCreateFrom() {
  var createBtn = document.querySelector('#create')
  createBtn.onclick = function() {
    var name = document.querySelector('input[name="name"]').value; 
    var description = document.querySelector('input[name="description"]').value;
    
    var formData = {
      name: name,
      description: description
    }

    createCourse(formData, function(){
      getCourses(renderCourses);
    });
  }
}

function handleDeleteCourse(id){
  var options = {
    method: 'DELETE',
    headers: {
      'Content-type': 'application/json'
    },

  };
  fetch(courseApi +'/' + id, options)
    .then(function(response){
      return response.json();
    })
    .then(function(){
     var course = document.querySelector('.course-item-'+ id);
     if(course){
      course.remove();
     }
    });
}


