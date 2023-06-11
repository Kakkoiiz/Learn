

var users = [
    {
        id: 1,
        name: 'Dung dz'
    },
    {
        id: 2,
        name: 'Dung1st'
    },
    {
        id: 3,
        name: 'Dung1stdz'
    }
]

var comments = [
    {
        id: 1,
        user_id: 1,
        content: 'Dung dz 1st'
    },
    {
        id: 2,
        user_id: 2,
        content: 'haha'
    }
]


function getUsersByIds(userIds) {
    return new Promise (function(resolve){
        var result = users.filter(function(user){
            return userIds.includes(user.id)
        })
        setTimeout(function(){
            resolve(result);
        }, 1000)
    })
}



function getComments() {
    return new Promise(function(resolve) {
        setTimeout(function() {
            resolve(comments);
        }, 1000)
    });
}

getComments(comments)
    .then(function(comments) {
        var userIds = comments.map(function(comment){
            return comment.user_id;
        })
        return getUsersByIds(userIds)
            .then(function(users){
                return {
                    users: users,
                    comments: comments,
                }
        });
    })

    .then(function(data){
        var commentBlock = document.getElementById('comment-block');

        var html = '';
        data.comments.forEach(function(comment){
            var user = data.users.find(function(user){
                return user.id === comment.user_id;
            });
        
            html += `${user.name}: ${comment.content}`
        });
        commentBlock.innerHTML = html

    })
