const tags = document.querySelector('#tags');
const newTag = document.querySelector('#newTag');

async function addNewTag(e) {
    if (e.code == 'Enter' || e.target.value) {

        const tagName = e.target.value.toLowerCase();

        const response = await fetch('/api/tags', {
            method: 'POST',
            body: JSON.stringify({
                tagName
            }),
            headers: {
                'Content-type': 'application/json'
            }
        });

        if (response.ok) {
            console.log(response);
            const newTagButton = document.createElement('button');
            newTagButton.classList.add('btn', 'btn-solid')
            newTagButton.setAttribute('type', 'button');
            newTagButton.innerText = tagName;
            tags.prepend(newTagButton);

            newTag.value = '';
        }
        else {
            alert(response.statusText);
        };
    }
}

const selectTags = function (e) {
    if (e.target.classList.contains('btn')) {

        if (e.target.classList.contains('btn-line')) {
            e.target.classList.remove('btn-line')
            e.target.classList.add('btn-solid');
        } else {
            e.target.classList.remove('btn-solid')
            e.target.classList.add('btn-line');
        };

    };
};

async function addPost(event) {
    event.preventDefault();

    const title = document.querySelector('#post-title').value;
    const body = document.querySelector('#post-body').value;

    const tagged = [];

    const selectedTags = tags.querySelectorAll('.btn-solid');
    console.log(selectedTags);

    for (let i = 0; i < selectedTags.length; i++) {
        let tagName = selectedTags[i].innerText.toLowerCase();
        console.log(tagName);
        tagged.push(tagName);
    }

    console.log(tagged);

    const response = await fetch('/api/posts', {
        method: 'POST',
        body: JSON.stringify({
            title,
            body,
            tagged
        }),
        headers: {
            'Content-type': 'application/json'
        }
    });

    if (response.ok) {
        console.log(response);
        document.location.replace('/dashboard');
    }
    else {
        alert(response.statusText);
    };
};

document.querySelector('.new-post-form').addEventListener('submit', addPost);

tags.addEventListener('click', selectTags);
newTag.addEventListener('blur', addNewTag);

