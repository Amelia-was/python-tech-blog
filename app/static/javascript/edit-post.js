async function editPost(event) {
    event.preventDefault();
    
    const title = document.querySelector('#post-title').value;
    const body = document.querySelector('#post-body').value;
    const id = document.location.href.split('/').pop();

    const response = await fetch(`/api/posts/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
            title,
            body
        }),
        headers: {
            'Content-type': 'application/json'
        }
    });

    if (response.ok) {
        document.location.replace('/dashboard');
    }
    else {
        alert(response.statusText);
    };
};

document.querySelector('.edit-post-form').addEventListener('submit', editPost);