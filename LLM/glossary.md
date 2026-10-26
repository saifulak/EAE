<a id="glossary"></a>
# Glossary

| Term | Brief description |
|---|---|
| virtual environment | A private folder of Python packages for one project, so versions do not clash. |
| kernel | The program that runs your notebook's code cells. |
| token | A small piece of text (a short word or part of one) that a model reads or writes. |
| prompt | The text you send to a model. |
| template | A prompt with blanks that you fill in each time. |
| schema | A written description of the shape and types a result must have. |
| embedding | A list of numbers that stands for the meaning of a text. |
| chunk | A small piece cut from a longer document. |
| retrieval | Finding the pieces of text most useful for a question. |
| agent | A program that lets a model choose steps and tools to reach a goal. |
| tool | A function an agent may call, such as a lookup or a calculator. |
| graph | Steps (nodes) joined by arrows (edges) that show the order of work. |
| node | One step in a graph. |
| edge | An arrow in a graph: where to go next. |
| trace | A short log of what each step did, how long it took and what it cost. |
| judge | A model asked to rate another model's answer. Useful, but it can be wrong too. |
| proxy | A company gateway between your PC and the internet. |
| redact | Remove or hide private details before text is shared. |
| injection | Hidden instructions inside text that try to steer a model. |
| golden set | A small set of questions with known good answers, used to check a helper. |
| stop budget | A hard limit (calls, steps or time) that makes a loop stop. |
| RAG | Retrieval-augmented generation: find the best text first, then let the model answer from it. |
| ReAct | Think, act, observe, repeat: a loop in which a model calls tools. |
| allow-list | The only tools or actions that may run; everything else is refused. |
| guard | A check that blocks a risky action or asks a human first. |
| supervisor / relay | Two ways to share work: one manager routes the tasks, or the agents hand a baton to each other. |
| hop budget | The most hand-offs a supervisor may make before it must stop. |
| thread id | A label for one conversation, so each chat keeps its own history. |
| recursion limit | LangGraph's step budget: the run stops with an error when it is reached. |
| state | The data a graph carries along and updates (here, the list of messages). |
| TF-IDF | A simple word-count method that turns text into numbers: similar wording gives similar numbers. |
| MMR | Maximal marginal relevance: pick results that are close to the question but different from each other. |
| held-out set | Questions kept hidden from the builders, so a test of the helper is fair. |
| regression | A change that breaks something that used to work. |