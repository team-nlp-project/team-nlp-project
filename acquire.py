"""
A module for obtaining repo readme and language data from the github API.

Before using this module, read through it, and follow the instructions marked
TODO.

After doing so, run it like this:

    python acquire.py

To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List, Optional, Union, cast
import requests

from env import github_token, github_username

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.

REPOS = ['josephmisiti/awesome-machine-learning',
 'microsoft/ML-For-Beginners',
 'bfortuner/ml-glossary',
 'trekhleb/homemade-machine-learning',
 'dangkhoasdc/awesome-ai-residency',
 'Spandan-Madan/DeepLearningProject',
 'roboticcam/machine-learning-notes',
 'ZuzooVn/machine-learning-for-software-engineers',
 'eugeneyan/applied-ml',
 'floodsung/Deep-Learning-Papers-Reading-Roadmap',
 'khangich/machine-learning-interview',
 'EthicalML/awesome-production-machine-learning',
 'Machine-Learning-Tokyo/Interactive_Tools',
 'GokuMohandas/MadeWithML',
 'ml-tooling/best-of-ml-python',
 'yandexdataschool/Practical_RL',
 'visenger/awesome-mlops',
 'aladdinpersson/Machine-Learning-Collection',
 'sshkhr/awesome-mlss',
 'ybayle/awesome-deep-learning-music',
 'eugeneyan/ml-surveys',
 'extreme-assistant/CVPR2021-Paper-Code-Interpretation',
 'ahkarami/Deep-Learning-in-Production',
 'labmlai/annotated_deep_learning_paper_implementations',
 'awesomedata/awesome-public-datasets',
 'jtoy/awesome-tensorflow',
 'kmario23/deep-learning-drizzle',
 'src-d/awesome-machine-learning-on-source-code',
 'manfreddiaz/awesome-autonomous-vehicles',
 'nashory/gans-awesome-applications',
 'jbhuang0604/awesome-computer-vision',
 'ritchieng/the-incredible-pytorch',
 'keon/awesome-nlp',
 'humphd/have-fun-with-machine-learning',
 'alirezadir/Production-Level-Deep-Learning',
 #'aikorea/awesome-rl/',
 'afshinea/stanford-cs-229-machine-learning',
 'terryum/awesome-deep-learning-papers',
 'zotroneneis/machine_learning_basics',
 'dustinvtran/ml-videos',
 #'JoseDeFreitas/awesome-youtubers#machine-learning',
 'ujjwalkarn/Machine-Learning-Tutorials',
 'ChristosChristofidis/awesome-deep-learning',
 'edobashira/speech-language-processing',
 'susanli2016/Machine-Learning-with-Python',
 'timzhang642/3D-Machine-Learning',
 'TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials',
 'firmai/industry-machine-learning',
 'dformoso/machine-learning-mindmap',
 'tirthajyoti/Machine-Learning-with-Python',
 'firmai/financial-machine-learning',
 'jphall663/awesome-machine-learning-interpretability',
 'krasserm/bayesian-machine-learning',
 'RedditSota/state-of-the-art-result-for-machine-learning-problems',
 'wtsxDev/Machine-Learning-for-Cyber-Security',
 'owainlewis/awesome-artificial-intelligence',
 'louisfb01/start-machine-learning',
 'ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code',
 'fritzlabs/Awesome-Mobile-Machine-Learning',
 'metrofun/machine-learning-surveys',
 'eriklindernoren/ML-From-Scratch',
 'HuaizhengZhang/Awesome-System-for-Machine-Learning',
 'grananqvist/Awesome-Quant-Machine-Learning-Trading',
 'jivoi/awesome-ml-for-cybersecurity',
 'rushter/MLAlgorithms',
 'huseinzol05/Stock-Prediction-Models',
 'lukas/ml-class',
 'huseinzol05/NLP-Models-Tensorflow',
 'kjw0612/awesome-deep-vision',
 'NirantK/awesome-project-ideas',
 'pliang279/awesome-multimodal-ml',
 'GoogleCloudPlatform/tensorflow-without-a-phd',
 'arbox/machine-learning-with-ruby',
 'naganandy/graph-based-deep-learning-literature',
 'weiaicunzai/awesome-image-classification',
 'sbrugman/deep-learning-papers',
 'abhineet123/Deep-Learning-for-Tracking-and-Detection',
 'DeepGraphLearning/LiteratureDL4Graph',
 'vinta/awesome-python',
 'spmallick/learnopencv',
 'AMAI-GmbH/AI-Expert-Roadmap',
 'heartexlabs/awesome-data-labeling',
 'MorvanZhou/Reinforcement-learning-with-tensorflow',
 'omarsar/nlp_overview',
 'mathsyouth/awesome-text-summarization',
 'benedekrozemberczki/awesome-community-detection',
 'D-X-Y/Awesome-AutoDL',
 'shaoxiongji/knowledge-graphs',
 'NiuTrans/ABigSurvey',
 'fuzhenxin/Style-Transfer-in-Text',
 'bharathgs/Awesome-pytorch-list',
 'thunlp/TAADpapers',
 'Kyubyong/nlp_tasks',
 #'Developer-Y/cs-video-courses#artificial-intelligence',
 'openMVG/awesome_3DReconstruction_list',
 'xinghaochen/awesome-hand-pose-estimation',
 'balavenkatesh3322/CV-pretrained-model',
 'hwalsuklee/awesome-deep-text-detection-recognition',
 'lzhbrian/image-to-image-papers',
 'sekwiatkowski/awesome-capsule-networks',
 'unrealcv/synthetic-computer-vision',
 'weihaox/awesome-neural-rendering',
 'dragen1860/TensorFlow-2.x-Tutorials',
 'AgaMiko/data-augmentation-review',
 'MaxBenChrist/awesome_time_series_in_python',
 'hoya012/awesome-anomaly-detection',
 'hibayesian/awesome-automl-papers',
 'cbailes/awesome-deep-trading',
 'jinwchoi/awesome-action-recognition',
 'amusi/awesome-object-detection',
 'rasbt/pattern_classification',
 'robmarkcole/satellite-image-deep-learning',
 'vahidk/EffectiveTensorflow',
 'Hvass-Labs/TensorFlow-Tutorials',
 'zhangqianhui/AdversarialNetsPapers',
 'dair-ai/nlp_paper_summaries',
 'mbadry1/DeepLearning.ai-Summary',
 'instillai/deep-learning-roadmap',
 'onnx/models',
 'jason718/awesome-self-supervised-learning',
 'microsoft/nlp-recipes',
 'poloclub/cnn-explainer',
 'ChanChiChoi/awesome-Face_Recognition',
 'aymericdamien/TopDeepLearning',
 'hongleizhang/RSPapers',
 'foolwood/benchmark_results',
 'wzhe06/Ad-papers',
 'andri27-ts/Reinforcement-Learning',
 'aleju/papers',
 'abhineet123/Deep-Learning-for-Tracking-and-Detection',
 'GauravBh1010tt/DeepLearn',
 'ageron/handson-ml',
 'Avik-Jain/100-Days-Of-ML-Code',
 'donnemartin/awesome-aws',
 'endymecy/awesome-deeplearning-resources',
 'likedan/Awesome-CoreML-Models',
 #'Vedenin/useful-java-links#ii-databases-search-engines-big-data-and-machine-learning',
 'hindupuravinash/the-gan-zoo',
 'benedekrozemberczki/awesome-decision-tree-papers',
 'rwightman/pytorch-image-models',
 'jslee02/awesome-robotics-libraries',
 'firmai/machine-learning-asset-management',
 'ahmedbahaaeldin/From-0-to-Research-Scientist-resources-guide',
 #'alirezadir/machine-learning-interview-enlightener/blob/main/README.md',
 'DeepGraphLearning/LiteratureDL4Graph',
 'ethen8181/machine-learning']

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        if "language" not in repo_info:
            raise Exception(
                "'language' key not round in response\n{}".format(json.dumps(repo_info))
            )
        return repo_info["language"]
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_download_url = get_readme_download_url(contents)
    if readme_download_url == "":
        readme_contents = ""
    else:
        readme_contents = requests.get(readme_download_url).text
    print(repo)
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data.json", "w"), indent=1)