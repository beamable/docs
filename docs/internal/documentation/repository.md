# Repository Structure

![repository.png](../../media/imgs/repository.png)

All documentation is consolidated within a single repository and Each iteration of the documentation is preserved in a distinct branch. The repository is divided into three primary branches: Core, Unity, and Unreal. Here is a brief overview of the repository structure:

- The **"Core"** branch encompasses common information, including Beamable concepts and the Command Line Interface (CLI).
- The **"Unity"** and **"Unreal"** branches are extensions of the **"Core"** branch and contain their respective sections. 
- The majority of modifications will take place in the most recent branch of each Software Development Kit (SDK). 
- Updates to the CLI or Beamable Concepts are incorporated into the Core branch and subsequently need to be merged into the correspondent SDK branches. 
- The entire process is managed using Git, which offers a familiar working environment. Developers can efficiently backport or forward fixes, cherry-pick, or merge versions, as all documentation is formatted in Markdown.

