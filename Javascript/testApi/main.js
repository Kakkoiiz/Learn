


var courseApi = 'http://localhost:3000/courses';

function start(){
    getCourses(renderCourses)
    
    handleCreateForm();
}

start();


function getCourses(callback){
    fetch(courseApi)
        .then(function(response) {
            return response.json(); 
        })
        .then(callback);
}


function createCourse(data, callback) {
    var options = {
        method: 'POST',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(data)
    
      };
      fetch(courseApi, options)
        .then((response) => response.json())
        .then(callback)
}

function handleCreateForm(){
    var createBtn = document.querySelector('#create');
    createBtn.onclick = function() {
        var name = document.querySelector('input[name="name"]').value;
        var description = document.querySelector('input[name="description"]').value;
        var formData = {
            name: name,
            description: description
        }

        createCourse(formData, function(){
            getCourses(renderCourses);
        })
    }
}


function handleDeleteCourse(id) {
    var options = {
        method: 'DELETE',
        headers: {
        'Content-type': 'application/json'
        },
    };
    fetch(courseApi + '/' + id, options)
        .then((response) => response.json())
        .then(() => {
            var course = document.querySelector('.course-item-' + id);
            if(course){
                course.remove();
            }
        });
}

function renderCourses(courses){
    var listCoursesBlock = document.querySelector('#list-courses');
    var htmls = courses.map((course) =>{
        return `
            <li class="course-item-${course.id}">
                <h4>${course.name}</h4>
                <p>${course.description}</->
                <button onclick="handleDeleteCourse(${course.id})">Xoa</button>
            </li> 
        `
    });
    listCoursesBlock.innerHTML = htmls.join('')
}

