---
description: Pull and merge the updates from remote main, solve the conflict gracefully
---

Please pull the latest code from the remote main and merge safely to my local feature branch, give a brief description on what have
  changed and say if that will affect the current implementation of the current feature branch.
  please make sure you understanding the codebase fully (and understand the code differences between current branch and the main branch) if there is conflict need to be solve, and you need to ask user for permission
  before solving conflict.\
  before you start merging you should invoke multiple agents to explore and review the changes to see if it will affect the current
  implementation (see current implementtation will use any of the changed parts and see if it will affect us)

  Don't take the results from the subagents as granted, think critically, please do cross verification your self and explore more related files if needed.

  For teh trategy to resolve conflict, you should look at what changes we have done to the current branch and think hard on how should you gracefully integrate the incomming main branch updates to our changed structure.

  for the merge commit message don't claim your auther ship in the message, please just include the essential merge message.