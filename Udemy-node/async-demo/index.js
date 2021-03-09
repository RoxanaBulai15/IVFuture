console.log('Before');
//setTimeout() este un exemplu de functie asincrona
// dupa 2 ecunde, va fi apelata functia
/*setTimeout(() => {
    console.log('Reading a user from a database...');
}, 2000);*/

// Asynchronous
/*getUser(1, (user) => {
    //console.log('User', user);
    // Get the repositories
    getRepositories(user.gitHubUsername, (repos) => {
        //console.log('Repos', repos);
        getCommits(repo, (commits) => {
            // CALLBACK HELL(Christmass tree)
        });
    });
});*/

getUser(1, getRepositories);

function getRepositories(user){
    getRepositories(user.gitHubUsername, getCommits);
}
function getCommits(repos) {
    getCommits(repo, displayCommits);
}
function displayCommits(commits) {
    console.log(commits);
}

// Synchronous
console.log('Before');
const user = getUser(1);
const repos = getRepositories(user.gitHubUsername);
const commits = getCommits(repos[0]);

console.log('After');

// Callbacks
// Promises
// Async/await

/*function getUser(id) {
    setTimeout(() => {
        console.log('Reading a user from a database...');
        return { id: id, gitHubUsername: 'mosh'};
    }, 2000);

    return 1;
}*/

// CALLBACK
function getUser(id, callback) {
    setTimeout(() => {
        console.log('Reading a user from a database...');
        callback({ id: id, gitHubUsername: 'mosh'});
    }, 2000);
}

function getRepositories(username, callback){
    setTimeout(() => {
        console.log('Calling GitHub API...');
        callback(['repo1', 'repo2', 'repo3']);
    }, 2000);
    return ['repo1', 'repo2', 'repo3'];
}