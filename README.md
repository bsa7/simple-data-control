# A simple ML pipeline with data versioning.

This project demonstrates the practical use of the dvc utility for working with data.

The problem statement uses a dataset from the “Titanic Disaster” contest.

## Receive code
To receive this repo to your computer, run:
```bash
cd ~/projects
git clone https://github.com/bsa7/simple-data-control.git
cd simple-data-control
```

## Working with data
For the data in the project, a folder with the name `data` is provided. This folder is not added to git and is intended for `dvс`, a data versioning tool [dvc](https://dvc.org/).

### Initialize local data storage
To load current data from google folder, use command:
```bash
mkdir data
dvc pull -r origin
```
This command will download data to your computer with the entire history of changes.

### Checkout between data versions
To navigate through the data history, use tags. You can view the list of tags using the command:
```bash
git tag
```
To switch to the selected version:
```bash
git checkout v2.0
dvc checkout
```
To switch back:
```bash
git checkout main
```

### Adding data changes to dvc
If your data has changed, add changes to the `dvc` with command:
```bash
dvc add data
```

Commit meta-information about data changes in a git:
```bash
git add data.dvc
git commit -m 'v1.1 - fill NA values in data'
git tag v1.1
git push origin HEAD
git push --tags origin
```

Push staged data changes to remote storage with command:
```bash
dvc push -r origin
```

### Other data manipulations
Pull data from remote storage with command:
```bash
dvc pull -r origin
```

If you need to undo changes you just made to your data, do it with:
```bash
dvc checkout
```
