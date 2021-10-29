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

REPOS = ['https://github.com/josephmisiti/awesome-machine-learning',
 'https://github.com/microsoft/ML-For-Beginners',
 'https://github.com/bfortuner/ml-glossary',
 'https://github.com/trekhleb/homemade-machine-learning',
 'https://github.com/dangkhoasdc/awesome-ai-residency',
 'https://github.com/Spandan-Madan/DeepLearningProject',
 'https://github.com/roboticcam/machine-learning-notes',
 'https://github.com/ZuzooVn/machine-learning-for-software-engineers',
 'https://github.com/eugeneyan/applied-ml',
 'https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap',
 'https://github.com/khangich/machine-learning-interview',
 'https://github.com/EthicalML/awesome-production-machine-learning',
 'https://github.com/Machine-Learning-Tokyo/Interactive_Tools',
 'https://github.com/GokuMohandas/MadeWithML',
 'https://github.com/ml-tooling/best-of-ml-python',
 'https://github.com/yandexdataschool/Practical_RL',
 'https://github.com/visenger/awesome-mlops',
 'https://github.com/aladdinpersson/Machine-Learning-Collection',
 'https://github.com/sshkhr/awesome-mlss',
 'https://github.com/ybayle/awesome-deep-learning-music',
 'https://github.com/eugeneyan/ml-surveys',
 'https://github.com/extreme-assistant/CVPR2021-Paper-Code-Interpretation',
 'https://github.com/ahkarami/Deep-Learning-in-Production',
 'https://github.com/labmlai/annotated_deep_learning_paper_implementations',
 'https://github.com/awesomedata/awesome-public-datasets',
 'https://github.com/jtoy/awesome-tensorflow',
 'https://github.com/kmario23/deep-learning-drizzle',
 'https://github.com/src-d/awesome-machine-learning-on-source-code',
 'https://github.com/manfreddiaz/awesome-autonomous-vehicles',
 'https://github.com/nashory/gans-awesome-applications',
 'https://github.com/jbhuang0604/awesome-computer-vision',
 'https://github.com/ritchieng/the-incredible-pytorch',
 'https://github.com/keon/awesome-nlp',
 'https://github.com/humphd/have-fun-with-machine-learning',
 'https://github.com/alirezadir/Production-Level-Deep-Learning',
 'https://github.com/aikorea/awesome-rl/',
 'https://github.com/afshinea/stanford-cs-229-machine-learning',
 'https://github.com/terryum/awesome-deep-learning-papers',
 'https://github.com/zotroneneis/machine_learning_basics',
 'https://github.com/dustinvtran/ml-videos',
 'https://github.com/JoseDeFreitas/awesome-youtubers#machine-learning',
 'https://github.com/ujjwalkarn/Machine-Learning-Tutorials',
 'https://github.com/ChristosChristofidis/awesome-deep-learning',
 'https://github.com/edobashira/speech-language-processing',
 'https://github.com/susanli2016/Machine-Learning-with-Python',
 'https://github.com/timzhang642/3D-Machine-Learning',
 'https://github.com/TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials',
 'https://github.com/firmai/industry-machine-learning',
 'https://github.com/dformoso/machine-learning-mindmap',
 'https://github.com/tirthajyoti/Machine-Learning-with-Python',
 'https://github.com/firmai/financial-machine-learning',
 'https://github.com/jphall663/awesome-machine-learning-interpretability',
 'https://github.com/krasserm/bayesian-machine-learning',
 'https://github.com/RedditSota/state-of-the-art-result-for-machine-learning-problems',
 'https://github.com/wtsxDev/Machine-Learning-for-Cyber-Security',
 'https://github.com/owainlewis/awesome-artificial-intelligence',
 'https://github.com/louisfb01/start-machine-learning',
 'https://github.com/ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code',
 'https://github.com/fritzlabs/Awesome-Mobile-Machine-Learning',
 'https://github.com/metrofun/machine-learning-surveys',
 'https://github.com/eriklindernoren/ML-From-Scratch',
 'https://github.com/HuaizhengZhang/Awesome-System-for-Machine-Learning',
 'https://github.com/grananqvist/Awesome-Quant-Machine-Learning-Trading',
 'https://github.com/jivoi/awesome-ml-for-cybersecurity',
 'https://github.com/rushter/MLAlgorithms',
 'https://github.com/huseinzol05/Stock-Prediction-Models',
 'https://github.com/lukas/ml-class',
 'https://github.com/huseinzol05/NLP-Models-Tensorflow',
 'https://github.com/kjw0612/awesome-deep-vision',
 'https://github.com/NirantK/awesome-project-ideas',
 'https://github.com/pliang279/awesome-multimodal-ml',
 'https://github.com/GoogleCloudPlatform/tensorflow-without-a-phd',
 'https://github.com/arbox/machine-learning-with-ruby',
 'https://github.com/naganandy/graph-based-deep-learning-literature',
 'https://github.com/weiaicunzai/awesome-image-classification',
 'https://github.com/sbrugman/deep-learning-papers',
 'https://github.com/abhineet123/Deep-Learning-for-Tracking-and-Detection',
 'https://github.com/DeepGraphLearning/LiteratureDL4Graph',
 'https://github.com/vinta/awesome-python',
 'https://github.com/spmallick/learnopencv',
 'https://github.com/AMAI-GmbH/AI-Expert-Roadmap',
 'https://github.com/heartexlabs/awesome-data-labeling',
 'https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow',
 'https://github.com/omarsar/nlp_overview',
 'https://github.com/mathsyouth/awesome-text-summarization',
 'https://github.com/benedekrozemberczki/awesome-community-detection',
 'https://github.com/D-X-Y/Awesome-AutoDL',
 'https://github.com/shaoxiongji/knowledge-graphs',
 'https://github.com/NiuTrans/ABigSurvey',
 'https://github.com/fuzhenxin/Style-Transfer-in-Text',
 'https://github.com/bharathgs/Awesome-pytorch-list',
 'https://github.com/thunlp/TAADpapers',
 'https://github.com/Kyubyong/nlp_tasks',
 'https://github.com/Developer-Y/cs-video-courses#artificial-intelligence',
 'https://github.com/openMVG/awesome_3DReconstruction_list',
 'https://github.com/xinghaochen/awesome-hand-pose-estimation',
 'https://github.com/balavenkatesh3322/CV-pretrained-model',
 'https://github.com/hwalsuklee/awesome-deep-text-detection-recognition',
 'https://github.com/lzhbrian/image-to-image-papers',
 'https://github.com/sekwiatkowski/awesome-capsule-networks',
 'https://github.com/unrealcv/synthetic-computer-vision',
 'https://github.com/weihaox/awesome-neural-rendering',
 'https://github.com/dragen1860/TensorFlow-2.x-Tutorials',
 'https://github.com/AgaMiko/data-augmentation-review',
 'https://github.com/MaxBenChrist/awesome_time_series_in_python',
 'https://github.com/hoya012/awesome-anomaly-detection',
 'https://github.com/hibayesian/awesome-automl-papers',
 'https://github.com/cbailes/awesome-deep-trading',
 'https://github.com/jinwchoi/awesome-action-recognition',
 'https://github.com/amusi/awesome-object-detection',
 'https://github.com/rasbt/pattern_classification',
 'https://github.com/robmarkcole/satellite-image-deep-learning',
 'https://github.com/vahidk/EffectiveTensorflow',
 'https://github.com/Hvass-Labs/TensorFlow-Tutorials',
 'https://github.com/zhangqianhui/AdversarialNetsPapers',
 'https://github.com/dair-ai/nlp_paper_summaries',
 'https://github.com/mbadry1/DeepLearning.ai-Summary',
 'https://github.com/instillai/deep-learning-roadmap',
 'https://github.com/onnx/models',
 'https://github.com/jason718/awesome-self-supervised-learning',
 'https://github.com/microsoft/nlp-recipes',
 'https://github.com/poloclub/cnn-explainer',
 'https://github.com/ChanChiChoi/awesome-Face_Recognition',
 'https://github.com/aymericdamien/TopDeepLearning',
 'https://github.com/hongleizhang/RSPapers',
 'https://github.com/foolwood/benchmark_results',
 'https://github.com/wzhe06/Ad-papers',
 'https://github.com/andri27-ts/Reinforcement-Learning',
 'https://github.com/aleju/papers',
 'https://github.com/abhineet123/Deep-Learning-for-Tracking-and-Detection',
 'https://github.com/GauravBh1010tt/DeepLearn',
 'https://github.com/ageron/handson-ml',
 'https://github.com/Avik-Jain/100-Days-Of-ML-Code',
 'https://github.com/donnemartin/awesome-aws',
 'https://github.com/endymecy/awesome-deeplearning-resources',
 'https://github.com/likedan/Awesome-CoreML-Models',
 'https://github.com/Vedenin/useful-java-links#ii-databases-search-engines-big-data-and-machine-learning',
 'https://github.com/hindupuravinash/the-gan-zoo',
 'https://github.com/benedekrozemberczki/awesome-decision-tree-papers',
 'https://github.com/rwightman/pytorch-image-models',
 'https://github.com/jslee02/awesome-robotics-libraries',
 'https://github.com/firmai/machine-learning-asset-management',
 'https://github.com/ahmedbahaaeldin/From-0-to-Research-Scientist-resources-guide',
 'https://github.com/alirezadir/machine-learning-interview-enlightener/blob/main/README.md',
 'https://github.com/DeepGraphLearning/LiteratureDL4Graph',
 'https://github.com/ethen8181/machine-learning']

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
