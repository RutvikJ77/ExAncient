import numpy as np
import tensorflow as tf
import os
from caption_model.config import Config
from caption_model.dataset import prepare_test_data
from caption_model.model import CaptionGenerator
from story_model import skipthoughts, decoder

from flask import Flask,render_template,request
app = Flask(__name__)

global passage
UPLOAD_FOLDER = '/Users/rutvik/Documents/Projects/KHE-neural/img2story_pretrain/image2story/test/images'

def model():
    config = Config()
    # ------test--------#
    tf.reset_default_graph()

    with tf.Session() as sess:
        model = CaptionGenerator(config)
        model.load(sess, config.model_file)
        tf.get_default_graph().finalize()
        data, vocabulary = prepare_test_data(config)
        info = model.test(sess, data, vocabulary)

    # story
    path = './story_model/stv_model/'
    encoder = skipthoughts.load_model(path, path)
    decode = decoder.load_model('./story_model/romance_models/romance.npz',
                                './story_model/romance_models/romance_dictionary.pkl')
    bneg = np.load('./story_model/romance_models/caption_style.npy')
    bpos = np.load('./story_model/romance_models/romance_style.npy')
    #passages = []
    for num in range(len(info)):
        sentence = info[num]['cap']
        # Compute skip-thought vectors for sentences
        svecs = skipthoughts.encode(encoder, sentence, verbose=False)
        # Style shifting
        shift = svecs.mean(0) - bneg + bpos
        passage = decoder.run_sampler(decode, shift, beam_width=3, maxlen=200)
        image_file = info[num]['img_path']
        #passages.append({'img': image_file, 'passage': passage})
        #print(passage)
        #print('done:%d' % num)
    print('Completed')
    #os.remove('./test/images/test1.jpg')
    return passage

@app.route('/',methods=['GET','POST'])
def upload_predict():
    if request.method == "POST":
        image_file = request.files['image']
        if image_file:
            image_location = os.path.join(UPLOAD_FOLDER,'test1.jpg') #Make sure the image filename is test1 and extension is .jpg
            image_file.save(image_location)
            passages = model()
            return render_template("index.html",story = passages)
    return render_template("index.html",story = "")


if __name__ == "__main__":
    app.run(port=5555,debug=True)