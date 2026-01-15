# Basic tmux commands

| command                               | description                    |
| ------------------------------------- | ------------------------------ |
| `tmux`                                | start new session              |
| `tmux new -s <session-name>`          | start named session            |
| `tmux ls`                             | list sessions                  |
| `tmux attach -t <session-name>`       | attach to named session        |
| `tmux attach`                         | attach to last session         |
| `tmux kill-session -t <session-name>` | kill named session             |
| `tmux kill-server`                    | kill all sessions              |
| `Ctrl+b d`                            | detach (keep session running)  |
| `exit`                                | end session (from inside tmux) |

# Window/pane management

| command                   | description      |
| ------------------------- | ---------------- |
| `Ctrl+b c`                | new window       |
| `Ctrl+b n`                | next window      |
| `Ctrl+b p`                | previous window  |
| `Ctrl+b <number>`         | go to window #   |
| `Ctrl+b ,`                | rename window    |
| `Ctrl+b &`                | close window     |
| `Ctrl+b "`                | split horizontal |
| `Ctrl+b %`                | split vertical   |
| `Ctrl+b <arrow>`          | switch panes     |
| `Ctrl+b` + hold `<arrow>` | resize pane      |
| `Ctrl+b x`                | close pane       |
