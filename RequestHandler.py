# -*- coding: utf-8 -*-


class RequestHandler():

    def __init__(self):
        pass

    def getResult(self, sentence):
        """1. Complete the classification in this function.

        Args:
            sentence: A string of sentence.

        Returns:
            classification: A string of the result of classification.
        """

        return "chat"

    def getBatchResults(self, sentencesList):
        """2. You can also complete the classification in this function,
                if you want to classify the sentences in batch.

        Args:
            sentencesList: A List of Dictionaries of ids and sentences,
                like:
                [{'id':331, 'content':'帮我打电话给张三' }, 
                 {'id':332, 'content':'帮我订一张机票!' },
                 ... ]

        Returns:
            resultsList: A List of Dictionaries of ids and results.
                The order of the list must be the same as the input list,
                like:
                [{'id':331, 'result':'telephone' }, 
                 {'id':332, 'result':'flight' },
                 ... ]
        """
        resultsList = []
        for sentence in sentencesList:
            resultDict = {}
            resultDict['id'] = sentence['id']
            resultDict['result'] = self.getResult(sentence['content'])
            resultsList.append(resultDict)

        return resultsList
