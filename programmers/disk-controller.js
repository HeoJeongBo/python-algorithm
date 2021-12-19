function solution(jobs) {
    var answer = 0,
        current = 0,
        time = 0;

    jobs.sort((a, b) => a[0] - b[0]);

    const priorityQ = [];

    while (current < jobs.length || priorityQ.length !== 0) {
        if (jobs.length > current && time >= jobs[current][0]) {
            priorityQ.push(jobs[current++]);
            priorityQ.sort((a, b) => a[1] - b[1]);
            continue;
        }
        if (priorityQ.length !== 0) {
            time += priorityQ[0][1];
            answer += time - priorityQ[0][0];
            priorityQ.shift();
        } else {
            time = jobs[current][0];
        }
    }

    return parseInt(answer / jobs.length, 10);
}
