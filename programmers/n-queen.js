function solution(n) {
    var answer = 0;
    const board = [];

    function hasConflict(row) {
        for (let i = 0; i < row; i++) {
            if (board[i] === board[row]) {
                return true;
            }
            if (Math.abs(board[row] - board[i]) === row - i) {
                return true;
            }
        }
        return false;
    }

    function dfs(row) {
        if (row === n) {
            answer++;
            return;
        }
        for (let col = 0; col < n; col++) {
            board[row] = col;
            if (!hasConflict(row)) {
                dfs(row + 1);
            }
        }
    }

    dfs(0);
    return answer;
}
