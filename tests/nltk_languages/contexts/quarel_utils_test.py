# pylint: disable=no-self-use,invalid-name
from ... import SemparseTestCase

from allennlp_semparse.common.knowledge_graph import KnowledgeGraph
from allennlp_semparse.nltk_languages.contexts.quarel_utils import get_explanation
from allennlp_semparse.nltk_languages.worlds.quarel_world import QuarelWorld


class TestQuarelUtils(SemparseTestCase):
    def test_get_explanation_provides_non_empty_explanation_for_typical_inputs(self):
        logical_form = '(infer (a:sugar higher world1) (a:diabetes higher world2) (a:diabetes higher world1))'
        entities = {'a:sugar': 'sugar', 'a:diabetes': 'diabetes'}
        world_extractions = {'world1': 'bill', 'world2': 'sue'}
        answer_index = 0
        knowledge_graph = KnowledgeGraph(entities.keys(), {key: [] for key in entities}, entities)
        world = QuarelWorld(knowledge_graph, "quarel_v1_attr_entities")
        explanation = get_explanation(logical_form,
                                      world_extractions,
                                      answer_index,
                                      world)
        assert len(explanation) == 4
