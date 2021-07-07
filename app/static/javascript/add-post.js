async function addPost (event) {
    event.preventDefault();

    const title = document.querySelector('#post-title').value;
    const body = document.querySelector('#post-body').value;
    const tags = [];
    
    const response = await fetch ('/api/posts', {
        method: 'POST',
        body: JSON.stringify({
            title,
            body,
            tags
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

document.querySelector('.new-post-form').addEventListener('submit', addPost);