# $ANTLR 3.5.3 C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g 2025-07-19 08:40:23

import sys
from antlr3 import *

from antlr3.tree import *




# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__94=94
T__95=95
T__96=96
T__97=97
T__98=98
T__99=99
T__100=100
T__101=101
T__102=102
T__103=103
ANDKW=4
ARGUMENT=5
ARGUMENTLIST=6
ASKW=7
ATKW=8
BYKW=9
CATCHESKW=10
CHOICEKW=11
COMMENT=12
CONTINUEKW=13
DIGIT=14
DOKW=15
EMPTY_ANNOTATION=16
EMPTY_ARGUMENT_LIST=17
EMPTY_LOCAL_CATCHES=18
EMPTY_LOCAL_THROW=19
EMPTY_MESSAGE_OP=20
EMPTY_MODULE_NAME=21
EMPTY_PARAMETER_DECL_LIST=22
EMPTY_SCOPE_NAME=23
EXTIDENTIFIER=24
FROMKW=25
GLOBALCHOICE=26
GLOBALCONTINUE=27
GLOBALDO=28
GLOBALINTERACTIONSEQUENCE=29
GLOBALINTERRUPT=30
GLOBALINTERRUPTIBLE=31
GLOBALKW=32
GLOBALMESSAGETRANSFER=33
GLOBALPARALLEL=34
GLOBALPROTOCOLBLOCK=35
GLOBALPROTOCOLDECL=36
GLOBALPROTOCOLDEF=37
GLOBALPROTOCOLINSTANCE=38
GLOBALRECURSION=39
IDENTIFIER=40
IMPORTKW=41
IMPORTMEMBER=42
IMPORTMODULE=43
INSTANTIATESKW=44
INTERRUPTIBLEKW=45
KIND_MESSAGE_SIGNATURE=46
KIND_PAYLOAD_TYPE=47
LETTER=48
LINE_COMMENT=49
LOCALCATCH=50
LOCALCHOICE=51
LOCALCONTINUE=52
LOCALDO=53
LOCALINTERACTIONSEQUENCE=54
LOCALINTERRUPT=55
LOCALINTERRUPTIBLE=56
LOCALKW=57
LOCALMESSAGETRANSFER=58
LOCALPARALLEL=59
LOCALPROTOCOLBLOCK=60
LOCALPROTOCOLDECL=61
LOCALPROTOCOLDEF=62
LOCALPROTOCOLINSTANCE=63
LOCALRECEIVE=64
LOCALRECURSION=65
LOCALSEND=66
LOCALTHROW=67
MESSAGESIGNATURE=68
MODULE=69
MODULEDECL=70
MODULEKW=71
ORKW=72
PARAMETERDECL=73
PARAMETERDECLLIST=74
PARKW=75
PAYLOAD=76
PAYLOADELEMENT=77
PAYLOADTYPEDECL=78
PROTOCOLKW=79
RECKW=80
ROLEDECL=81
ROLEDECLLIST=82
ROLEINSTANTIATION=83
ROLEINSTANTIATIONLIST=84
ROLEKW=85
SIGKW=86
SYMBOL=87
THROWSKW=88
TOKW=89
TYPEKW=90
UNDERSCORE=91
WHITESPACE=92
WITHKW=93

# token names
tokenNamesMap = {
    0: "<invalid>", 1: "<EOR>", 2: "<DOWN>", 3: "<UP>",
    -1: "EOF", 94: "T__94", 95: "T__95", 96: "T__96", 97: "T__97", 98: "T__98", 
    99: "T__99", 100: "T__100", 101: "T__101", 102: "T__102", 103: "T__103", 
    4: "ANDKW", 5: "ARGUMENT", 6: "ARGUMENTLIST", 7: "ASKW", 8: "ATKW", 
    9: "BYKW", 10: "CATCHESKW", 11: "CHOICEKW", 12: "COMMENT", 13: "CONTINUEKW", 
    14: "DIGIT", 15: "DOKW", 16: "EMPTY_ANNOTATION", 17: "EMPTY_ARGUMENT_LIST", 
    18: "EMPTY_LOCAL_CATCHES", 19: "EMPTY_LOCAL_THROW", 20: "EMPTY_MESSAGE_OP", 
    21: "EMPTY_MODULE_NAME", 22: "EMPTY_PARAMETER_DECL_LIST", 23: "EMPTY_SCOPE_NAME", 
    24: "EXTIDENTIFIER", 25: "FROMKW", 26: "GLOBALCHOICE", 27: "GLOBALCONTINUE", 
    28: "GLOBALDO", 29: "GLOBALINTERACTIONSEQUENCE", 30: "GLOBALINTERRUPT", 
    31: "GLOBALINTERRUPTIBLE", 32: "GLOBALKW", 33: "GLOBALMESSAGETRANSFER", 
    34: "GLOBALPARALLEL", 35: "GLOBALPROTOCOLBLOCK", 36: "GLOBALPROTOCOLDECL", 
    37: "GLOBALPROTOCOLDEF", 38: "GLOBALPROTOCOLINSTANCE", 39: "GLOBALRECURSION", 
    40: "IDENTIFIER", 41: "IMPORTKW", 42: "IMPORTMEMBER", 43: "IMPORTMODULE", 
    44: "INSTANTIATESKW", 45: "INTERRUPTIBLEKW", 46: "KIND_MESSAGE_SIGNATURE", 
    47: "KIND_PAYLOAD_TYPE", 48: "LETTER", 49: "LINE_COMMENT", 50: "LOCALCATCH", 
    51: "LOCALCHOICE", 52: "LOCALCONTINUE", 53: "LOCALDO", 54: "LOCALINTERACTIONSEQUENCE", 
    55: "LOCALINTERRUPT", 56: "LOCALINTERRUPTIBLE", 57: "LOCALKW", 58: "LOCALMESSAGETRANSFER", 
    59: "LOCALPARALLEL", 60: "LOCALPROTOCOLBLOCK", 61: "LOCALPROTOCOLDECL", 
    62: "LOCALPROTOCOLDEF", 63: "LOCALPROTOCOLINSTANCE", 64: "LOCALRECEIVE", 
    65: "LOCALRECURSION", 66: "LOCALSEND", 67: "LOCALTHROW", 68: "MESSAGESIGNATURE", 
    69: "MODULE", 70: "MODULEDECL", 71: "MODULEKW", 72: "ORKW", 73: "PARAMETERDECL", 
    74: "PARAMETERDECLLIST", 75: "PARKW", 76: "PAYLOAD", 77: "PAYLOADELEMENT", 
    78: "PAYLOADTYPEDECL", 79: "PROTOCOLKW", 80: "RECKW", 81: "ROLEDECL", 
    82: "ROLEDECLLIST", 83: "ROLEINSTANTIATION", 84: "ROLEINSTANTIATIONLIST", 
    85: "ROLEKW", 86: "SIGKW", 87: "SYMBOL", 88: "THROWSKW", 89: "TOKW", 
    90: "TYPEKW", 91: "UNDERSCORE", 92: "WHITESPACE", 93: "WITHKW"
}


# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ANDKW", "ARGUMENT", "ARGUMENTLIST", "ASKW", "ATKW", "BYKW", "CATCHESKW", 
    "CHOICEKW", "COMMENT", "CONTINUEKW", "DIGIT", "DOKW", "EMPTY_ANNOTATION", 
    "EMPTY_ARGUMENT_LIST", "EMPTY_LOCAL_CATCHES", "EMPTY_LOCAL_THROW", "EMPTY_MESSAGE_OP", 
    "EMPTY_MODULE_NAME", "EMPTY_PARAMETER_DECL_LIST", "EMPTY_SCOPE_NAME", 
    "EXTIDENTIFIER", "FROMKW", "GLOBALCHOICE", "GLOBALCONTINUE", "GLOBALDO", 
    "GLOBALINTERACTIONSEQUENCE", "GLOBALINTERRUPT", "GLOBALINTERRUPTIBLE", 
    "GLOBALKW", "GLOBALMESSAGETRANSFER", "GLOBALPARALLEL", "GLOBALPROTOCOLBLOCK", 
    "GLOBALPROTOCOLDECL", "GLOBALPROTOCOLDEF", "GLOBALPROTOCOLINSTANCE", 
    "GLOBALRECURSION", "IDENTIFIER", "IMPORTKW", "IMPORTMEMBER", "IMPORTMODULE", 
    "INSTANTIATESKW", "INTERRUPTIBLEKW", "KIND_MESSAGE_SIGNATURE", "KIND_PAYLOAD_TYPE", 
    "LETTER", "LINE_COMMENT", "LOCALCATCH", "LOCALCHOICE", "LOCALCONTINUE", 
    "LOCALDO", "LOCALINTERACTIONSEQUENCE", "LOCALINTERRUPT", "LOCALINTERRUPTIBLE", 
    "LOCALKW", "LOCALMESSAGETRANSFER", "LOCALPARALLEL", "LOCALPROTOCOLBLOCK", 
    "LOCALPROTOCOLDECL", "LOCALPROTOCOLDEF", "LOCALPROTOCOLINSTANCE", "LOCALRECEIVE", 
    "LOCALRECURSION", "LOCALSEND", "LOCALTHROW", "MESSAGESIGNATURE", "MODULE", 
    "MODULEDECL", "MODULEKW", "ORKW", "PARAMETERDECL", "PARAMETERDECLLIST", 
    "PARKW", "PAYLOAD", "PAYLOADELEMENT", "PAYLOADTYPEDECL", "PROTOCOLKW", 
    "RECKW", "ROLEDECL", "ROLEDECLLIST", "ROLEINSTANTIATION", "ROLEINSTANTIATIONLIST", 
    "ROLEKW", "SIGKW", "SYMBOL", "THROWSKW", "TOKW", "TYPEKW", "UNDERSCORE", 
    "WHITESPACE", "WITHKW", "'('", "')'", "','", "'.'", "':'", "';'", "'<'", 
    "'>'", "'{'", "'}'"
]



class ScribbleParser(Parser):
    grammarFileName = "C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super().__init__(input, state, *args, **kwargs)

        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )

        self.dfa10 = self.DFA10(
            self, 10,
            eot = self.DFA10_eot,
            eof = self.DFA10_eof,
            min = self.DFA10_min,
            max = self.DFA10_max,
            accept = self.DFA10_accept,
            special = self.DFA10_special,
            transition = self.DFA10_transition
            )

        self.dfa17 = self.DFA17(
            self, 17,
            eot = self.DFA17_eot,
            eof = self.DFA17_eof,
            min = self.DFA17_min,
            max = self.DFA17_max,
            accept = self.DFA17_accept,
            special = self.DFA17_special,
            transition = self.DFA17_transition
            )

        self.dfa23 = self.DFA23(
            self, 23,
            eot = self.DFA23_eot,
            eof = self.DFA23_eof,
            min = self.DFA23_min,
            max = self.DFA23_max,
            accept = self.DFA23_accept,
            special = self.DFA23_special,
            transition = self.DFA23_transition
            )

        self.dfa27 = self.DFA27(
            self, 27,
            eot = self.DFA27_eot,
            eof = self.DFA27_eof,
            min = self.DFA27_min,
            max = self.DFA27_max,
            accept = self.DFA27_accept,
            special = self.DFA27_special,
            transition = self.DFA27_transition
            )

        self.dfa38 = self.DFA38(
            self, 38,
            eot = self.DFA38_eot,
            eof = self.DFA38_eof,
            min = self.DFA38_min,
            max = self.DFA38_max,
            accept = self.DFA38_accept,
            special = self.DFA38_special,
            transition = self.DFA38_transition
            )

        self.dfa39 = self.DFA39(
            self, 39,
            eot = self.DFA39_eot,
            eof = self.DFA39_eof,
            min = self.DFA39_min,
            max = self.DFA39_max,
            accept = self.DFA39_accept,
            special = self.DFA39_special,
            transition = self.DFA39_transition
            )

        self.dfa41 = self.DFA41(
            self, 41,
            eot = self.DFA41_eot,
            eof = self.DFA41_eof,
            min = self.DFA41_min,
            max = self.DFA41_max,
            accept = self.DFA41_accept,
            special = self.DFA41_special,
            transition = self.DFA41_transition
            )

        self.dfa43 = self.DFA43(
            self, 43,
            eot = self.DFA43_eot,
            eof = self.DFA43_eof,
            min = self.DFA43_min,
            max = self.DFA43_max,
            accept = self.DFA43_accept,
            special = self.DFA43_special,
            transition = self.DFA43_transition
            )

        self.dfa53 = self.DFA53(
            self, 53,
            eot = self.DFA53_eot,
            eof = self.DFA53_eof,
            min = self.DFA53_min,
            max = self.DFA53_max,
            accept = self.DFA53_accept,
            special = self.DFA53_special,
            transition = self.DFA53_transition
            )




        self.delegates = []

        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class rolename_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "rolename"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:201:1: rolename : IDENTIFIER ;
    def rolename(self, ):
        retval = self.rolename_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IDENTIFIER1 = None

        IDENTIFIER1_tree = None

        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:201:9: ( IDENTIFIER )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:201:11: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()


                IDENTIFIER1 = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_rolename998)
                if self._state.backtracking == 0:
                    IDENTIFIER1_tree = self._adaptor.createWithPayload(IDENTIFIER1)
                    self._adaptor.addChild(root_0, IDENTIFIER1_tree)





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "rolename"


    class payloadtypename_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "payloadtypename"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:202:1: payloadtypename : IDENTIFIER ;
    def payloadtypename(self, ):
        retval = self.payloadtypename_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IDENTIFIER2 = None

        IDENTIFIER2_tree = None

        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:202:16: ( IDENTIFIER )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:202:18: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()


                IDENTIFIER2 = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_payloadtypename1004)
                if self._state.backtracking == 0:
                    IDENTIFIER2_tree = self._adaptor.createWithPayload(IDENTIFIER2)
                    self._adaptor.addChild(root_0, IDENTIFIER2_tree)





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "payloadtypename"


    class protocolname_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "protocolname"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:203:1: protocolname : IDENTIFIER ;
    def protocolname(self, ):
        retval = self.protocolname_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IDENTIFIER3 = None

        IDENTIFIER3_tree = None

        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:203:13: ( IDENTIFIER )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:203:15: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()


                IDENTIFIER3 = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_protocolname1010)
                if self._state.backtracking == 0:
                    IDENTIFIER3_tree = self._adaptor.createWithPayload(IDENTIFIER3)
                    self._adaptor.addChild(root_0, IDENTIFIER3_tree)





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "protocolname"


    class parametername_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "parametername"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:204:1: parametername : IDENTIFIER ;
    def parametername(self, ):
        retval = self.parametername_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IDENTIFIER4 = None

        IDENTIFIER4_tree = None

        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:204:14: ( IDENTIFIER )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:204:16: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()


                IDENTIFIER4 = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_parametername1016)
                if self._state.backtracking == 0:
                    IDENTIFIER4_tree = self._adaptor.createWithPayload(IDENTIFIER4)
                    self._adaptor.addChild(root_0, IDENTIFIER4_tree)





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "parametername"


    class annotationname_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "annotationname"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:205:1: annotationname : IDENTIFIER ;
    def annotationname(self, ):
        retval = self.annotationname_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IDENTIFIER5 = None

        IDENTIFIER5_tree = None

        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:205:15: ( IDENTIFIER )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:205:17: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()


                IDENTIFIER5 = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_annotationname1022)
                if self._state.backtracking == 0:
                    IDENTIFIER5_tree = self._adaptor.createWithPayload(IDENTIFIER5)
                    self._adaptor.addChild(root_0, IDENTIFIER5_tree)





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "annotationname"


    class recursionlabelname_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "recursionlabelname"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:206:1: recursionlabelname : IDENTIFIER ;
    def recursionlabelname(self, ):
        retval = self.recursionlabelname_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IDENTIFIER6 = None

        IDENTIFIER6_tree = None

        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:206:19: ( IDENTIFIER )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:206:21: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()


                IDENTIFIER6 = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_recursionlabelname1028)
                if self._state.backtracking == 0:
                    IDENTIFIER6_tree = self._adaptor.createWithPayload(IDENTIFIER6)
                    self._adaptor.addChild(root_0, IDENTIFIER6_tree)





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "recursionlabelname"


    class scopename_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "scopename"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:207:1: scopename : IDENTIFIER ;
    def scopename(self, ):
        retval = self.scopename_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IDENTIFIER7 = None

        IDENTIFIER7_tree = None

        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:207:10: ( IDENTIFIER )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:207:12: IDENTIFIER
                pass 
                root_0 = self._adaptor.nil()


                IDENTIFIER7 = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_scopename1034)
                if self._state.backtracking == 0:
                    IDENTIFIER7_tree = self._adaptor.createWithPayload(IDENTIFIER7)
                    self._adaptor.addChild(root_0, IDENTIFIER7_tree)





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "scopename"


    class modulename_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "modulename"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:219:1: modulename : ( IDENTIFIER ( '.' IDENTIFIER )* '.' IDENTIFIER -> ( IDENTIFIER )+ | IDENTIFIER -> ( IDENTIFIER )+ );
    def modulename(self, ):
        retval = self.modulename_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IDENTIFIER8 = None
        char_literal9 = None
        IDENTIFIER10 = None
        char_literal11 = None
        IDENTIFIER12 = None
        IDENTIFIER13 = None

        IDENTIFIER8_tree = None
        char_literal9_tree = None
        IDENTIFIER10_tree = None
        char_literal11_tree = None
        IDENTIFIER12_tree = None
        IDENTIFIER13_tree = None
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_97 = RewriteRuleTokenStream(self._adaptor, "token 97")

        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:219:11: ( IDENTIFIER ( '.' IDENTIFIER )* '.' IDENTIFIER -> ( IDENTIFIER )+ | IDENTIFIER -> ( IDENTIFIER )+ )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == IDENTIFIER) :
                    LA2_1 = self.input.LA(2)

                    if (LA2_1 == 97) :
                        LA2_2 = self.input.LA(3)

                        if (LA2_2 == IDENTIFIER) :
                            LA2_4 = self.input.LA(4)

                            if (LA2_4 in {ASKW, IMPORTKW, 97, 99}) :
                                alt2 = 1
                            elif (LA2_4 in {94, 100}) :
                                alt2 = 2
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                nvae = NoViableAltException("", 2, 4, self.input)

                                raise nvae


                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 2, 2, self.input)

                            raise nvae


                    elif (LA2_1 in {ASKW, IMPORTKW, 99}) :
                        alt2 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 2, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae


                if alt2 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:221:2: IDENTIFIER ( '.' IDENTIFIER )* '.' IDENTIFIER
                    pass 
                    IDENTIFIER8 = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_modulename1050) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER8)


                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:221:13: ( '.' IDENTIFIER )*
                    while True: #loop1
                        alt1 = 2
                        LA1_0 = self.input.LA(1)

                        if (LA1_0 == 97) :
                            LA1_1 = self.input.LA(2)

                            if (LA1_1 == IDENTIFIER) :
                                LA1_2 = self.input.LA(3)

                                if (LA1_2 == 97) :
                                    LA1_3 = self.input.LA(4)

                                    if (LA1_3 == IDENTIFIER) :
                                        LA1_5 = self.input.LA(5)

                                        if (LA1_5 in {ASKW, IMPORTKW, 97, 99}) :
                                            alt1 = 1










                        if alt1 == 1:
                            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:221:14: '.' IDENTIFIER
                            pass 
                            char_literal9 = self.match(self.input, 97, self.FOLLOW_97_in_modulename1053) 
                            if self._state.backtracking == 0:
                                stream_97.add(char_literal9)


                            IDENTIFIER10 = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_modulename1055) 
                            if self._state.backtracking == 0:
                                stream_IDENTIFIER.add(IDENTIFIER10)



                        else:
                            break #loop1


                    char_literal11 = self.match(self.input, 97, self.FOLLOW_97_in_modulename1059) 
                    if self._state.backtracking == 0:
                        stream_97.add(char_literal11)


                    IDENTIFIER12 = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_modulename1061) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER12)


                    # AST Rewrite
                    # elements: IDENTIFIER
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 222:2: -> ( IDENTIFIER )+
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:223:2: ( IDENTIFIER )+
                        if not (stream_IDENTIFIER.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_IDENTIFIER.hasNext():
                            self._adaptor.addChild(root_0, 
                            stream_IDENTIFIER.nextNode()
                            )


                        stream_IDENTIFIER.reset()




                        retval.tree = root_0




                elif alt2 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:225:2: IDENTIFIER
                    pass 
                    IDENTIFIER13 = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_modulename1075) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER13)


                    # AST Rewrite
                    # elements: IDENTIFIER
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 226:2: -> ( IDENTIFIER )+
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:227:2: ( IDENTIFIER )+
                        if not (stream_IDENTIFIER.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_IDENTIFIER.hasNext():
                            self._adaptor.addChild(root_0, 
                            stream_IDENTIFIER.nextNode()
                            )


                        stream_IDENTIFIER.reset()




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "modulename"


    class membername_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "membername"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:230:1: membername : ( simplemembername | fullmembername );
    def membername(self, ):
        retval = self.membername_return()
        retval.start = self.input.LT(1)


        root_0 = None

        simplemembername14 = None
        fullmembername15 = None


        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:230:11: ( simplemembername | fullmembername )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == IDENTIFIER) :
                    LA3_1 = self.input.LA(2)

                    if (LA3_1 in {94, 100}) :
                        alt3 = 1
                    elif (LA3_1 == 97) :
                        alt3 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 3, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:231:2: simplemembername
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_simplemembername_in_membername1093)
                    simplemembername14 = self.simplemembername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, simplemembername14.tree)



                elif alt3 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:233:2: fullmembername
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_fullmembername_in_membername1098)
                    fullmembername15 = self.fullmembername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, fullmembername15.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "membername"


    class simplemembername_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "simplemembername"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:236:1: simplemembername : ( payloadtypename | protocolname );
    def simplemembername(self, ):
        retval = self.simplemembername_return()
        retval.start = self.input.LT(1)


        root_0 = None

        payloadtypename16 = None
        protocolname17 = None


        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:236:17: ( payloadtypename | protocolname )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == IDENTIFIER) :
                    LA4_1 = self.input.LA(2)

                    if (self.synpred4_Scribble()) :
                        alt4 = 1
                    elif (True) :
                        alt4 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 4, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae


                if alt4 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:237:2: payloadtypename
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_payloadtypename_in_simplemembername1107)
                    payloadtypename16 = self.payloadtypename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, payloadtypename16.tree)



                elif alt4 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:239:2: protocolname
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_protocolname_in_simplemembername1112)
                    protocolname17 = self.protocolname()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, protocolname17.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "simplemembername"


    class fullmembername_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "fullmembername"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:244:1: fullmembername : modulename '.' simplemembername -> modulename simplemembername ;
    def fullmembername(self, ):
        retval = self.fullmembername_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal19 = None
        modulename18 = None
        simplemembername20 = None

        char_literal19_tree = None
        stream_97 = RewriteRuleTokenStream(self._adaptor, "token 97")
        stream_modulename = RewriteRuleSubtreeStream(self._adaptor, "rule modulename")
        stream_simplemembername = RewriteRuleSubtreeStream(self._adaptor, "rule simplemembername")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:244:15: ( modulename '.' simplemembername -> modulename simplemembername )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:245:2: modulename '.' simplemembername
                pass 
                self._state.following.append(self.FOLLOW_modulename_in_fullmembername1124)
                modulename18 = self.modulename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_modulename.add(modulename18.tree)


                char_literal19 = self.match(self.input, 97, self.FOLLOW_97_in_fullmembername1126) 
                if self._state.backtracking == 0:
                    stream_97.add(char_literal19)


                self._state.following.append(self.FOLLOW_simplemembername_in_fullmembername1128)
                simplemembername20 = self.simplemembername()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_simplemembername.add(simplemembername20.tree)


                # AST Rewrite
                # elements: simplemembername, modulename
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 248:2: -> modulename simplemembername
                    self._adaptor.addChild(root_0, stream_modulename.nextTree())

                    self._adaptor.addChild(root_0, stream_simplemembername.nextTree())




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "fullmembername"


    class module_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "module"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:256:1: module : moduledecl ( importdecl )* ( payloadtypedecl )* ( protocoldecl )* -> ^( MODULE moduledecl ( importdecl )* ( payloadtypedecl )* ( protocoldecl )* ) ;
    def module(self, ):
        retval = self.module_return()
        retval.start = self.input.LT(1)


        root_0 = None

        moduledecl21 = None
        importdecl22 = None
        payloadtypedecl23 = None
        protocoldecl24 = None

        stream_protocoldecl = RewriteRuleSubtreeStream(self._adaptor, "rule protocoldecl")
        stream_payloadtypedecl = RewriteRuleSubtreeStream(self._adaptor, "rule payloadtypedecl")
        stream_importdecl = RewriteRuleSubtreeStream(self._adaptor, "rule importdecl")
        stream_moduledecl = RewriteRuleSubtreeStream(self._adaptor, "rule moduledecl")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:256:7: ( moduledecl ( importdecl )* ( payloadtypedecl )* ( protocoldecl )* -> ^( MODULE moduledecl ( importdecl )* ( payloadtypedecl )* ( protocoldecl )* ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:257:2: moduledecl ( importdecl )* ( payloadtypedecl )* ( protocoldecl )*
                pass 
                self._state.following.append(self.FOLLOW_moduledecl_in_module1151)
                moduledecl21 = self.moduledecl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_moduledecl.add(moduledecl21.tree)


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:257:13: ( importdecl )*
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if (LA5_0 in {FROMKW, IMPORTKW}) :
                        alt5 = 1


                    if alt5 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:257:14: importdecl
                        pass 
                        self._state.following.append(self.FOLLOW_importdecl_in_module1154)
                        importdecl22 = self.importdecl()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_importdecl.add(importdecl22.tree)



                    else:
                        break #loop5


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:257:27: ( payloadtypedecl )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == TYPEKW) :
                        alt6 = 1


                    if alt6 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:257:28: payloadtypedecl
                        pass 
                        self._state.following.append(self.FOLLOW_payloadtypedecl_in_module1159)
                        payloadtypedecl23 = self.payloadtypedecl()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_payloadtypedecl.add(payloadtypedecl23.tree)



                    else:
                        break #loop6


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:257:46: ( protocoldecl )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 in {GLOBALKW, LOCALKW}) :
                        alt7 = 1


                    if alt7 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:257:47: protocoldecl
                        pass 
                        self._state.following.append(self.FOLLOW_protocoldecl_in_module1164)
                        protocoldecl24 = self.protocoldecl()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_protocoldecl.add(protocoldecl24.tree)



                    else:
                        break #loop7


                # AST Rewrite
                # elements: payloadtypedecl, importdecl, protocoldecl, moduledecl
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 258:2: -> ^( MODULE moduledecl ( importdecl )* ( payloadtypedecl )* ( protocoldecl )* )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:261:2: ^( MODULE moduledecl ( importdecl )* ( payloadtypedecl )* ( protocoldecl )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(MODULE, "MODULE")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_moduledecl.nextTree())

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:261:22: ( importdecl )*
                    while stream_importdecl.hasNext():
                        self._adaptor.addChild(root_1, stream_importdecl.nextTree())


                    stream_importdecl.reset();

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:261:36: ( payloadtypedecl )*
                    while stream_payloadtypedecl.hasNext():
                        self._adaptor.addChild(root_1, stream_payloadtypedecl.nextTree())


                    stream_payloadtypedecl.reset();

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:261:55: ( protocoldecl )*
                    while stream_protocoldecl.hasNext():
                        self._adaptor.addChild(root_1, stream_protocoldecl.nextTree())


                    stream_protocoldecl.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "module"


    class moduledecl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "moduledecl"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:270:1: moduledecl : MODULEKW modulename ';' -> ^( MODULEDECL modulename ) ;
    def moduledecl(self, ):
        retval = self.moduledecl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        MODULEKW25 = None
        char_literal27 = None
        modulename26 = None

        MODULEKW25_tree = None
        char_literal27_tree = None
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_MODULEKW = RewriteRuleTokenStream(self._adaptor, "token MODULEKW")
        stream_modulename = RewriteRuleSubtreeStream(self._adaptor, "rule modulename")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:270:11: ( MODULEKW modulename ';' -> ^( MODULEDECL modulename ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:271:2: MODULEKW modulename ';'
                pass 
                MODULEKW25 = self.match(self.input, MODULEKW, self.FOLLOW_MODULEKW_in_moduledecl1209) 
                if self._state.backtracking == 0:
                    stream_MODULEKW.add(MODULEKW25)


                self._state.following.append(self.FOLLOW_modulename_in_moduledecl1211)
                modulename26 = self.modulename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_modulename.add(modulename26.tree)


                char_literal27 = self.match(self.input, 99, self.FOLLOW_99_in_moduledecl1213) 
                if self._state.backtracking == 0:
                    stream_99.add(char_literal27)


                # AST Rewrite
                # elements: modulename
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 272:2: -> ^( MODULEDECL modulename )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:273:2: ^( MODULEDECL modulename )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(MODULEDECL, "MODULEDECL")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_modulename.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "moduledecl"


    class importdecl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "importdecl"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:280:1: importdecl : ( importmodule | importmember );
    def importdecl(self, ):
        retval = self.importdecl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        importmodule28 = None
        importmember29 = None


        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:280:11: ( importmodule | importmember )
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == IMPORTKW) :
                    alt8 = 1
                elif (LA8_0 == FROMKW) :
                    alt8 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae


                if alt8 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:281:2: importmodule
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_importmodule_in_importdecl1235)
                    importmodule28 = self.importmodule()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, importmodule28.tree)



                elif alt8 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:283:2: importmember
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_importmember_in_importdecl1240)
                    importmember29 = self.importmember()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, importmember29.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "importdecl"


    class importmodule_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "importmodule"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:286:1: importmodule : ( IMPORTKW modulename ';' -> ^( IMPORTMODULE modulename ) | IMPORTKW modulename ASKW IDENTIFIER ';' -> ^( IMPORTMODULE ASKW IDENTIFIER modulename ) );
    def importmodule(self, ):
        retval = self.importmodule_return()
        retval.start = self.input.LT(1)


        root_0 = None

        IMPORTKW30 = None
        char_literal32 = None
        IMPORTKW33 = None
        ASKW35 = None
        IDENTIFIER36 = None
        char_literal37 = None
        modulename31 = None
        modulename34 = None

        IMPORTKW30_tree = None
        char_literal32_tree = None
        IMPORTKW33_tree = None
        ASKW35_tree = None
        IDENTIFIER36_tree = None
        char_literal37_tree = None
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_ASKW = RewriteRuleTokenStream(self._adaptor, "token ASKW")
        stream_IMPORTKW = RewriteRuleTokenStream(self._adaptor, "token IMPORTKW")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_modulename = RewriteRuleSubtreeStream(self._adaptor, "rule modulename")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:286:13: ( IMPORTKW modulename ';' -> ^( IMPORTMODULE modulename ) | IMPORTKW modulename ASKW IDENTIFIER ';' -> ^( IMPORTMODULE ASKW IDENTIFIER modulename ) )
                alt9 = 2
                alt9 = self.dfa9.predict(self.input)
                if alt9 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:287:2: IMPORTKW modulename ';'
                    pass 
                    IMPORTKW30 = self.match(self.input, IMPORTKW, self.FOLLOW_IMPORTKW_in_importmodule1249) 
                    if self._state.backtracking == 0:
                        stream_IMPORTKW.add(IMPORTKW30)


                    self._state.following.append(self.FOLLOW_modulename_in_importmodule1251)
                    modulename31 = self.modulename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_modulename.add(modulename31.tree)


                    char_literal32 = self.match(self.input, 99, self.FOLLOW_99_in_importmodule1253) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal32)


                    # AST Rewrite
                    # elements: modulename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 288:2: -> ^( IMPORTMODULE modulename )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:289:2: ^( IMPORTMODULE modulename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(IMPORTMODULE, "IMPORTMODULE")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_modulename.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt9 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:292:2: IMPORTKW modulename ASKW IDENTIFIER ';'
                    pass 
                    IMPORTKW33 = self.match(self.input, IMPORTKW, self.FOLLOW_IMPORTKW_in_importmodule1271) 
                    if self._state.backtracking == 0:
                        stream_IMPORTKW.add(IMPORTKW33)


                    self._state.following.append(self.FOLLOW_modulename_in_importmodule1273)
                    modulename34 = self.modulename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_modulename.add(modulename34.tree)


                    ASKW35 = self.match(self.input, ASKW, self.FOLLOW_ASKW_in_importmodule1275) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW35)


                    IDENTIFIER36 = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_importmodule1277) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER36)


                    char_literal37 = self.match(self.input, 99, self.FOLLOW_99_in_importmodule1279) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal37)


                    # AST Rewrite
                    # elements: IDENTIFIER, modulename, ASKW
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 293:2: -> ^( IMPORTMODULE ASKW IDENTIFIER modulename )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:294:2: ^( IMPORTMODULE ASKW IDENTIFIER modulename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(IMPORTMODULE, "IMPORTMODULE")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        stream_ASKW.nextNode()
                        )

                        self._adaptor.addChild(root_1, 
                        stream_IDENTIFIER.nextNode()
                        )

                        self._adaptor.addChild(root_1, stream_modulename.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "importmodule"


    class importmember_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "importmember"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:298:1: importmember : ( FROMKW modulename IMPORTKW simplemembername ';' -> ^( IMPORTMEMBER simplemembername modulename ) | FROMKW modulename IMPORTKW simplemembername ASKW IDENTIFIER ';' -> ^( IMPORTMEMBER ASKW IDENTIFIER simplemembername modulename ) );
    def importmember(self, ):
        retval = self.importmember_return()
        retval.start = self.input.LT(1)


        root_0 = None

        FROMKW38 = None
        IMPORTKW40 = None
        char_literal42 = None
        FROMKW43 = None
        IMPORTKW45 = None
        ASKW47 = None
        IDENTIFIER48 = None
        char_literal49 = None
        modulename39 = None
        simplemembername41 = None
        modulename44 = None
        simplemembername46 = None

        FROMKW38_tree = None
        IMPORTKW40_tree = None
        char_literal42_tree = None
        FROMKW43_tree = None
        IMPORTKW45_tree = None
        ASKW47_tree = None
        IDENTIFIER48_tree = None
        char_literal49_tree = None
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_ASKW = RewriteRuleTokenStream(self._adaptor, "token ASKW")
        stream_IMPORTKW = RewriteRuleTokenStream(self._adaptor, "token IMPORTKW")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_FROMKW = RewriteRuleTokenStream(self._adaptor, "token FROMKW")
        stream_modulename = RewriteRuleSubtreeStream(self._adaptor, "rule modulename")
        stream_simplemembername = RewriteRuleSubtreeStream(self._adaptor, "rule simplemembername")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:298:13: ( FROMKW modulename IMPORTKW simplemembername ';' -> ^( IMPORTMEMBER simplemembername modulename ) | FROMKW modulename IMPORTKW simplemembername ASKW IDENTIFIER ';' -> ^( IMPORTMEMBER ASKW IDENTIFIER simplemembername modulename ) )
                alt10 = 2
                alt10 = self.dfa10.predict(self.input)
                if alt10 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:299:2: FROMKW modulename IMPORTKW simplemembername ';'
                    pass 
                    FROMKW38 = self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_importmember1350) 
                    if self._state.backtracking == 0:
                        stream_FROMKW.add(FROMKW38)


                    self._state.following.append(self.FOLLOW_modulename_in_importmember1352)
                    modulename39 = self.modulename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_modulename.add(modulename39.tree)


                    IMPORTKW40 = self.match(self.input, IMPORTKW, self.FOLLOW_IMPORTKW_in_importmember1354) 
                    if self._state.backtracking == 0:
                        stream_IMPORTKW.add(IMPORTKW40)


                    self._state.following.append(self.FOLLOW_simplemembername_in_importmember1356)
                    simplemembername41 = self.simplemembername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_simplemembername.add(simplemembername41.tree)


                    char_literal42 = self.match(self.input, 99, self.FOLLOW_99_in_importmember1358) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal42)


                    # AST Rewrite
                    # elements: simplemembername, modulename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 300:2: -> ^( IMPORTMEMBER simplemembername modulename )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:301:2: ^( IMPORTMEMBER simplemembername modulename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(IMPORTMEMBER, "IMPORTMEMBER")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_simplemembername.nextTree())

                        self._adaptor.addChild(root_1, stream_modulename.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt10 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:304:2: FROMKW modulename IMPORTKW simplemembername ASKW IDENTIFIER ';'
                    pass 
                    FROMKW43 = self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_importmember1424) 
                    if self._state.backtracking == 0:
                        stream_FROMKW.add(FROMKW43)


                    self._state.following.append(self.FOLLOW_modulename_in_importmember1426)
                    modulename44 = self.modulename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_modulename.add(modulename44.tree)


                    IMPORTKW45 = self.match(self.input, IMPORTKW, self.FOLLOW_IMPORTKW_in_importmember1428) 
                    if self._state.backtracking == 0:
                        stream_IMPORTKW.add(IMPORTKW45)


                    self._state.following.append(self.FOLLOW_simplemembername_in_importmember1430)
                    simplemembername46 = self.simplemembername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_simplemembername.add(simplemembername46.tree)


                    ASKW47 = self.match(self.input, ASKW, self.FOLLOW_ASKW_in_importmember1432) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW47)


                    IDENTIFIER48 = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_importmember1434) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER48)


                    char_literal49 = self.match(self.input, 99, self.FOLLOW_99_in_importmember1436) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal49)


                    # AST Rewrite
                    # elements: ASKW, IDENTIFIER, modulename, simplemembername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 305:2: -> ^( IMPORTMEMBER ASKW IDENTIFIER simplemembername modulename )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:306:2: ^( IMPORTMEMBER ASKW IDENTIFIER simplemembername modulename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(IMPORTMEMBER, "IMPORTMEMBER")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        stream_ASKW.nextNode()
                        )

                        self._adaptor.addChild(root_1, 
                        stream_IDENTIFIER.nextNode()
                        )

                        self._adaptor.addChild(root_1, stream_simplemembername.nextTree())

                        self._adaptor.addChild(root_1, stream_modulename.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "importmember"


    class payloadtypedecl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "payloadtypedecl"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:314:1: payloadtypedecl : TYPEKW '<' IDENTIFIER '>' EXTIDENTIFIER FROMKW EXTIDENTIFIER ASKW payloadtypename ';' -> ^( PAYLOADTYPEDECL IDENTIFIER EXTIDENTIFIER EXTIDENTIFIER payloadtypename ) ;
    def payloadtypedecl(self, ):
        retval = self.payloadtypedecl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPEKW50 = None
        char_literal51 = None
        IDENTIFIER52 = None
        char_literal53 = None
        EXTIDENTIFIER54 = None
        FROMKW55 = None
        EXTIDENTIFIER56 = None
        ASKW57 = None
        char_literal59 = None
        payloadtypename58 = None

        TYPEKW50_tree = None
        char_literal51_tree = None
        IDENTIFIER52_tree = None
        char_literal53_tree = None
        EXTIDENTIFIER54_tree = None
        FROMKW55_tree = None
        EXTIDENTIFIER56_tree = None
        ASKW57_tree = None
        char_literal59_tree = None
        stream_ASKW = RewriteRuleTokenStream(self._adaptor, "token ASKW")
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_100 = RewriteRuleTokenStream(self._adaptor, "token 100")
        stream_101 = RewriteRuleTokenStream(self._adaptor, "token 101")
        stream_TYPEKW = RewriteRuleTokenStream(self._adaptor, "token TYPEKW")
        stream_EXTIDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token EXTIDENTIFIER")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_FROMKW = RewriteRuleTokenStream(self._adaptor, "token FROMKW")
        stream_payloadtypename = RewriteRuleSubtreeStream(self._adaptor, "rule payloadtypename")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:314:16: ( TYPEKW '<' IDENTIFIER '>' EXTIDENTIFIER FROMKW EXTIDENTIFIER ASKW payloadtypename ';' -> ^( PAYLOADTYPEDECL IDENTIFIER EXTIDENTIFIER EXTIDENTIFIER payloadtypename ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:315:2: TYPEKW '<' IDENTIFIER '>' EXTIDENTIFIER FROMKW EXTIDENTIFIER ASKW payloadtypename ';'
                pass 
                TYPEKW50 = self.match(self.input, TYPEKW, self.FOLLOW_TYPEKW_in_payloadtypedecl1466) 
                if self._state.backtracking == 0:
                    stream_TYPEKW.add(TYPEKW50)


                char_literal51 = self.match(self.input, 100, self.FOLLOW_100_in_payloadtypedecl1468) 
                if self._state.backtracking == 0:
                    stream_100.add(char_literal51)


                IDENTIFIER52 = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_payloadtypedecl1470) 
                if self._state.backtracking == 0:
                    stream_IDENTIFIER.add(IDENTIFIER52)


                char_literal53 = self.match(self.input, 101, self.FOLLOW_101_in_payloadtypedecl1472) 
                if self._state.backtracking == 0:
                    stream_101.add(char_literal53)


                EXTIDENTIFIER54 = self.match(self.input, EXTIDENTIFIER, self.FOLLOW_EXTIDENTIFIER_in_payloadtypedecl1474) 
                if self._state.backtracking == 0:
                    stream_EXTIDENTIFIER.add(EXTIDENTIFIER54)


                FROMKW55 = self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_payloadtypedecl1476) 
                if self._state.backtracking == 0:
                    stream_FROMKW.add(FROMKW55)


                EXTIDENTIFIER56 = self.match(self.input, EXTIDENTIFIER, self.FOLLOW_EXTIDENTIFIER_in_payloadtypedecl1478) 
                if self._state.backtracking == 0:
                    stream_EXTIDENTIFIER.add(EXTIDENTIFIER56)


                ASKW57 = self.match(self.input, ASKW, self.FOLLOW_ASKW_in_payloadtypedecl1480) 
                if self._state.backtracking == 0:
                    stream_ASKW.add(ASKW57)


                self._state.following.append(self.FOLLOW_payloadtypename_in_payloadtypedecl1482)
                payloadtypename58 = self.payloadtypename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_payloadtypename.add(payloadtypename58.tree)


                char_literal59 = self.match(self.input, 99, self.FOLLOW_99_in_payloadtypedecl1484) 
                if self._state.backtracking == 0:
                    stream_99.add(char_literal59)


                # AST Rewrite
                # elements: EXTIDENTIFIER, EXTIDENTIFIER, IDENTIFIER, payloadtypename
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 316:2: -> ^( PAYLOADTYPEDECL IDENTIFIER EXTIDENTIFIER EXTIDENTIFIER payloadtypename )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:317:2: ^( PAYLOADTYPEDECL IDENTIFIER EXTIDENTIFIER EXTIDENTIFIER payloadtypename )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(PAYLOADTYPEDECL, "PAYLOADTYPEDECL")
                    , root_1)

                    self._adaptor.addChild(root_1, 
                    stream_IDENTIFIER.nextNode()
                    )

                    self._adaptor.addChild(root_1, 
                    stream_EXTIDENTIFIER.nextNode()
                    )

                    self._adaptor.addChild(root_1, 
                    stream_EXTIDENTIFIER.nextNode()
                    )

                    self._adaptor.addChild(root_1, stream_payloadtypename.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "payloadtypedecl"


    class messageoperator_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "messageoperator"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:326:1: messageoperator : ( LETTER | DIGIT | UNDERSCORE )+ ;
    def messageoperator(self, ):
        retval = self.messageoperator_return()
        retval.start = self.input.LT(1)


        root_0 = None

        set60 = None

        set60_tree = None

        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:326:16: ( ( LETTER | DIGIT | UNDERSCORE )+ )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:327:2: ( LETTER | DIGIT | UNDERSCORE )+
                pass 
                root_0 = self._adaptor.nil()


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:327:2: ( LETTER | DIGIT | UNDERSCORE )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 in {DIGIT, LETTER, UNDERSCORE}) :
                        alt11 = 1


                    if alt11 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:
                        pass 
                        set60 = self.input.LT(1)

                        if self.input.LA(1) in {DIGIT, LETTER, UNDERSCORE}:
                            self.input.consume()
                            if self._state.backtracking == 0:
                                self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set60))

                            self._state.errorRecovery = False


                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            mse = MismatchedSetException(None, self.input)
                            raise mse




                    else:
                        if cnt11 >= 1:
                            break #loop11

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "messageoperator"


    class messagesignature_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "messagesignature"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:330:1: messagesignature : ( '(' payload ')' -> ^( MESSAGESIGNATURE EMPTY_MESSAGE_OP payload ) | IDENTIFIER '(' payload ')' -> ^( MESSAGESIGNATURE IDENTIFIER payload ) );
    def messagesignature(self, ):
        retval = self.messagesignature_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal61 = None
        char_literal63 = None
        IDENTIFIER64 = None
        char_literal65 = None
        char_literal67 = None
        payload62 = None
        payload66 = None

        char_literal61_tree = None
        char_literal63_tree = None
        IDENTIFIER64_tree = None
        char_literal65_tree = None
        char_literal67_tree = None
        stream_94 = RewriteRuleTokenStream(self._adaptor, "token 94")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_payload = RewriteRuleSubtreeStream(self._adaptor, "rule payload")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:330:17: ( '(' payload ')' -> ^( MESSAGESIGNATURE EMPTY_MESSAGE_OP payload ) | IDENTIFIER '(' payload ')' -> ^( MESSAGESIGNATURE IDENTIFIER payload ) )
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if (LA12_0 == 94) :
                    alt12 = 1
                elif (LA12_0 == IDENTIFIER) :
                    alt12 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 12, 0, self.input)

                    raise nvae


                if alt12 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:331:2: '(' payload ')'
                    pass 
                    char_literal61 = self.match(self.input, 94, self.FOLLOW_94_in_messagesignature1536) 
                    if self._state.backtracking == 0:
                        stream_94.add(char_literal61)


                    self._state.following.append(self.FOLLOW_payload_in_messagesignature1538)
                    payload62 = self.payload()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_payload.add(payload62.tree)


                    char_literal63 = self.match(self.input, 95, self.FOLLOW_95_in_messagesignature1540) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal63)


                    # AST Rewrite
                    # elements: payload
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 332:2: -> ^( MESSAGESIGNATURE EMPTY_MESSAGE_OP payload )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:333:2: ^( MESSAGESIGNATURE EMPTY_MESSAGE_OP payload )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(MESSAGESIGNATURE, "MESSAGESIGNATURE")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(EMPTY_MESSAGE_OP, "EMPTY_MESSAGE_OP")
                        )

                        self._adaptor.addChild(root_1, stream_payload.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt12 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:336:2: IDENTIFIER '(' payload ')'
                    pass 
                    IDENTIFIER64 = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_messagesignature1559) 
                    if self._state.backtracking == 0:
                        stream_IDENTIFIER.add(IDENTIFIER64)


                    char_literal65 = self.match(self.input, 94, self.FOLLOW_94_in_messagesignature1561) 
                    if self._state.backtracking == 0:
                        stream_94.add(char_literal65)


                    self._state.following.append(self.FOLLOW_payload_in_messagesignature1563)
                    payload66 = self.payload()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_payload.add(payload66.tree)


                    char_literal67 = self.match(self.input, 95, self.FOLLOW_95_in_messagesignature1565) 
                    if self._state.backtracking == 0:
                        stream_95.add(char_literal67)


                    # AST Rewrite
                    # elements: IDENTIFIER, payload
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 337:2: -> ^( MESSAGESIGNATURE IDENTIFIER payload )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:339:2: ^( MESSAGESIGNATURE IDENTIFIER payload )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(MESSAGESIGNATURE, "MESSAGESIGNATURE")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        stream_IDENTIFIER.nextNode()
                        )

                        self._adaptor.addChild(root_1, stream_payload.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "messagesignature"


    class payload_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "payload"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:342:1: payload : ( -> ^( PAYLOAD ) | payloadelement ( ',' payloadelement )* -> ^( PAYLOAD ( payloadelement )+ ) );
    def payload(self, ):
        retval = self.payload_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal69 = None
        payloadelement68 = None
        payloadelement70 = None

        char_literal69_tree = None
        stream_96 = RewriteRuleTokenStream(self._adaptor, "token 96")
        stream_payloadelement = RewriteRuleSubtreeStream(self._adaptor, "rule payloadelement")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:342:8: ( -> ^( PAYLOAD ) | payloadelement ( ',' payloadelement )* -> ^( PAYLOAD ( payloadelement )+ ) )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == 95) :
                    alt14 = 1
                elif (LA14_0 == IDENTIFIER) :
                    alt14 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae


                if alt14 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:343:2: 
                    pass 
                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 343:2: -> ^( PAYLOAD )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:344:2: ^( PAYLOAD )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(PAYLOAD, "PAYLOAD")
                        , root_1)

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt14 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:346:2: payloadelement ( ',' payloadelement )*
                    pass 
                    self._state.following.append(self.FOLLOW_payloadelement_in_payload1598)
                    payloadelement68 = self.payloadelement()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_payloadelement.add(payloadelement68.tree)


                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:346:17: ( ',' payloadelement )*
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == 96) :
                            alt13 = 1


                        if alt13 == 1:
                            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:346:18: ',' payloadelement
                            pass 
                            char_literal69 = self.match(self.input, 96, self.FOLLOW_96_in_payload1601) 
                            if self._state.backtracking == 0:
                                stream_96.add(char_literal69)


                            self._state.following.append(self.FOLLOW_payloadelement_in_payload1603)
                            payloadelement70 = self.payloadelement()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_payloadelement.add(payloadelement70.tree)



                        else:
                            break #loop13


                    # AST Rewrite
                    # elements: payloadelement
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 347:2: -> ^( PAYLOAD ( payloadelement )+ )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:348:2: ^( PAYLOAD ( payloadelement )+ )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(PAYLOAD, "PAYLOAD")
                        , root_1)

                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:348:12: ( payloadelement )+
                        if not (stream_payloadelement.hasNext()):
                            raise RewriteEarlyExitException()

                        while stream_payloadelement.hasNext():
                            self._adaptor.addChild(root_1, stream_payloadelement.nextTree())


                        stream_payloadelement.reset()

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "payload"


    class payloadelement_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "payloadelement"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:351:1: payloadelement : ( payloadtypename -> ^( PAYLOADELEMENT EMPTY_ANNOTATION payloadtypename ) | parametername -> ^( PAYLOADELEMENT EMPTY_ANNOTATION parametername ) | annotationname ':' payloadtypename -> ^( PAYLOADELEMENT annotationname payloadtypename ) | annotationname ':' parametername -> ^( PAYLOADELEMENT annotationname parametername ) );
    def payloadelement(self, ):
        retval = self.payloadelement_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal74 = None
        char_literal77 = None
        payloadtypename71 = None
        parametername72 = None
        annotationname73 = None
        payloadtypename75 = None
        annotationname76 = None
        parametername78 = None

        char_literal74_tree = None
        char_literal77_tree = None
        stream_98 = RewriteRuleTokenStream(self._adaptor, "token 98")
        stream_annotationname = RewriteRuleSubtreeStream(self._adaptor, "rule annotationname")
        stream_parametername = RewriteRuleSubtreeStream(self._adaptor, "rule parametername")
        stream_payloadtypename = RewriteRuleSubtreeStream(self._adaptor, "rule payloadtypename")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:351:15: ( payloadtypename -> ^( PAYLOADELEMENT EMPTY_ANNOTATION payloadtypename ) | parametername -> ^( PAYLOADELEMENT EMPTY_ANNOTATION parametername ) | annotationname ':' payloadtypename -> ^( PAYLOADELEMENT annotationname payloadtypename ) | annotationname ':' parametername -> ^( PAYLOADELEMENT annotationname parametername ) )
                alt15 = 4
                LA15_0 = self.input.LA(1)

                if (LA15_0 == IDENTIFIER) :
                    LA15_1 = self.input.LA(2)

                    if (LA15_1 == 98) :
                        LA15_2 = self.input.LA(3)

                        if (LA15_2 == IDENTIFIER) :
                            LA15_5 = self.input.LA(4)

                            if (self.synpred19_Scribble()) :
                                alt15 = 3
                            elif (True) :
                                alt15 = 4
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                nvae = NoViableAltException("", 15, 5, self.input)

                                raise nvae


                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 15, 2, self.input)

                            raise nvae


                    elif (self.synpred17_Scribble()) :
                        alt15 = 1
                    elif (self.synpred18_Scribble()) :
                        alt15 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 15, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 15, 0, self.input)

                    raise nvae


                if alt15 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:352:2: payloadtypename
                    pass 
                    self._state.following.append(self.FOLLOW_payloadtypename_in_payloadelement1627)
                    payloadtypename71 = self.payloadtypename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_payloadtypename.add(payloadtypename71.tree)


                    # AST Rewrite
                    # elements: payloadtypename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 353:2: -> ^( PAYLOADELEMENT EMPTY_ANNOTATION payloadtypename )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:354:2: ^( PAYLOADELEMENT EMPTY_ANNOTATION payloadtypename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(PAYLOADELEMENT, "PAYLOADELEMENT")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(EMPTY_ANNOTATION, "EMPTY_ANNOTATION")
                        )

                        self._adaptor.addChild(root_1, stream_payloadtypename.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt15 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:356:2: parametername
                    pass 
                    self._state.following.append(self.FOLLOW_parametername_in_payloadelement1644)
                    parametername72 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername72.tree)


                    # AST Rewrite
                    # elements: parametername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 358:2: -> ^( PAYLOADELEMENT EMPTY_ANNOTATION parametername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:359:2: ^( PAYLOADELEMENT EMPTY_ANNOTATION parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(PAYLOADELEMENT, "PAYLOADELEMENT")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(EMPTY_ANNOTATION, "EMPTY_ANNOTATION")
                        )

                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt15 == 3:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:361:2: annotationname ':' payloadtypename
                    pass 
                    self._state.following.append(self.FOLLOW_annotationname_in_payloadelement1664)
                    annotationname73 = self.annotationname()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_annotationname.add(annotationname73.tree)


                    char_literal74 = self.match(self.input, 98, self.FOLLOW_98_in_payloadelement1666) 
                    if self._state.backtracking == 0:
                        stream_98.add(char_literal74)


                    self._state.following.append(self.FOLLOW_payloadtypename_in_payloadelement1668)
                    payloadtypename75 = self.payloadtypename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_payloadtypename.add(payloadtypename75.tree)


                    # AST Rewrite
                    # elements: payloadtypename, annotationname
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 362:2: -> ^( PAYLOADELEMENT annotationname payloadtypename )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:363:2: ^( PAYLOADELEMENT annotationname payloadtypename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(PAYLOADELEMENT, "PAYLOADELEMENT")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_annotationname.nextTree())

                        self._adaptor.addChild(root_1, stream_payloadtypename.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt15 == 4:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:365:2: annotationname ':' parametername
                    pass 
                    self._state.following.append(self.FOLLOW_annotationname_in_payloadelement1685)
                    annotationname76 = self.annotationname()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_annotationname.add(annotationname76.tree)


                    char_literal77 = self.match(self.input, 98, self.FOLLOW_98_in_payloadelement1687) 
                    if self._state.backtracking == 0:
                        stream_98.add(char_literal77)


                    self._state.following.append(self.FOLLOW_parametername_in_payloadelement1689)
                    parametername78 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername78.tree)


                    # AST Rewrite
                    # elements: annotationname, parametername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 366:2: -> ^( PAYLOADELEMENT annotationname parametername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:367:2: ^( PAYLOADELEMENT annotationname parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(PAYLOADELEMENT, "PAYLOADELEMENT")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_annotationname.nextTree())

                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "payloadelement"


    class protocoldecl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "protocoldecl"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:374:1: protocoldecl : ( globalprotocoldecl | localprotocoldecl );
    def protocoldecl(self, ):
        retval = self.protocoldecl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        globalprotocoldecl79 = None
        localprotocoldecl80 = None


        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:374:13: ( globalprotocoldecl | localprotocoldecl )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == GLOBALKW) :
                    alt16 = 1
                elif (LA16_0 == LOCALKW) :
                    alt16 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae


                if alt16 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:375:2: globalprotocoldecl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_globalprotocoldecl_in_protocoldecl1713)
                    globalprotocoldecl79 = self.globalprotocoldecl()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, globalprotocoldecl79.tree)



                elif alt16 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:377:2: localprotocoldecl
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_localprotocoldecl_in_protocoldecl1718)
                    localprotocoldecl80 = self.localprotocoldecl()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localprotocoldecl80.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "protocoldecl"


    class globalprotocoldecl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "globalprotocoldecl"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:384:1: globalprotocoldecl : ( globalprotocolheader globalprotocoldefinition -> ^( GLOBALPROTOCOLDECL globalprotocolheader globalprotocoldefinition ) | globalprotocolheader globalprotocolinstance -> ^( GLOBALPROTOCOLDECL globalprotocolheader globalprotocolinstance ) );
    def globalprotocoldecl(self, ):
        retval = self.globalprotocoldecl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        globalprotocolheader81 = None
        globalprotocoldefinition82 = None
        globalprotocolheader83 = None
        globalprotocolinstance84 = None

        stream_globalprotocoldefinition = RewriteRuleSubtreeStream(self._adaptor, "rule globalprotocoldefinition")
        stream_globalprotocolinstance = RewriteRuleSubtreeStream(self._adaptor, "rule globalprotocolinstance")
        stream_globalprotocolheader = RewriteRuleSubtreeStream(self._adaptor, "rule globalprotocolheader")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:384:19: ( globalprotocolheader globalprotocoldefinition -> ^( GLOBALPROTOCOLDECL globalprotocolheader globalprotocoldefinition ) | globalprotocolheader globalprotocolinstance -> ^( GLOBALPROTOCOLDECL globalprotocolheader globalprotocolinstance ) )
                alt17 = 2
                alt17 = self.dfa17.predict(self.input)
                if alt17 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:385:3: globalprotocolheader globalprotocoldefinition
                    pass 
                    self._state.following.append(self.FOLLOW_globalprotocolheader_in_globalprotocoldecl1731)
                    globalprotocolheader81 = self.globalprotocolheader()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_globalprotocolheader.add(globalprotocolheader81.tree)


                    self._state.following.append(self.FOLLOW_globalprotocoldefinition_in_globalprotocoldecl1733)
                    globalprotocoldefinition82 = self.globalprotocoldefinition()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_globalprotocoldefinition.add(globalprotocoldefinition82.tree)


                    # AST Rewrite
                    # elements: globalprotocolheader, globalprotocoldefinition
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 386:2: -> ^( GLOBALPROTOCOLDECL globalprotocolheader globalprotocoldefinition )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:387:2: ^( GLOBALPROTOCOLDECL globalprotocolheader globalprotocoldefinition )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(GLOBALPROTOCOLDECL, "GLOBALPROTOCOLDECL")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_globalprotocolheader.nextTree())

                        self._adaptor.addChild(root_1, stream_globalprotocoldefinition.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt17 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:389:2: globalprotocolheader globalprotocolinstance
                    pass 
                    self._state.following.append(self.FOLLOW_globalprotocolheader_in_globalprotocoldecl1750)
                    globalprotocolheader83 = self.globalprotocolheader()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_globalprotocolheader.add(globalprotocolheader83.tree)


                    self._state.following.append(self.FOLLOW_globalprotocolinstance_in_globalprotocoldecl1752)
                    globalprotocolinstance84 = self.globalprotocolinstance()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_globalprotocolinstance.add(globalprotocolinstance84.tree)


                    # AST Rewrite
                    # elements: globalprotocolheader, globalprotocolinstance
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 390:2: -> ^( GLOBALPROTOCOLDECL globalprotocolheader globalprotocolinstance )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:391:2: ^( GLOBALPROTOCOLDECL globalprotocolheader globalprotocolinstance )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(GLOBALPROTOCOLDECL, "GLOBALPROTOCOLDECL")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_globalprotocolheader.nextTree())

                        self._adaptor.addChild(root_1, stream_globalprotocolinstance.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "globalprotocoldecl"


    class globalprotocolheader_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "globalprotocolheader"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:394:1: globalprotocolheader : ( GLOBALKW PROTOCOLKW protocolname roledecllist -> protocolname EMPTY_PARAMETER_DECL_LIST roledecllist | GLOBALKW PROTOCOLKW protocolname parameterdecllist roledecllist -> protocolname parameterdecllist roledecllist );
    def globalprotocolheader(self, ):
        retval = self.globalprotocolheader_return()
        retval.start = self.input.LT(1)


        root_0 = None

        GLOBALKW85 = None
        PROTOCOLKW86 = None
        GLOBALKW89 = None
        PROTOCOLKW90 = None
        protocolname87 = None
        roledecllist88 = None
        protocolname91 = None
        parameterdecllist92 = None
        roledecllist93 = None

        GLOBALKW85_tree = None
        PROTOCOLKW86_tree = None
        GLOBALKW89_tree = None
        PROTOCOLKW90_tree = None
        stream_GLOBALKW = RewriteRuleTokenStream(self._adaptor, "token GLOBALKW")
        stream_PROTOCOLKW = RewriteRuleTokenStream(self._adaptor, "token PROTOCOLKW")
        stream_roledecllist = RewriteRuleSubtreeStream(self._adaptor, "rule roledecllist")
        stream_protocolname = RewriteRuleSubtreeStream(self._adaptor, "rule protocolname")
        stream_parameterdecllist = RewriteRuleSubtreeStream(self._adaptor, "rule parameterdecllist")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:394:21: ( GLOBALKW PROTOCOLKW protocolname roledecllist -> protocolname EMPTY_PARAMETER_DECL_LIST roledecllist | GLOBALKW PROTOCOLKW protocolname parameterdecllist roledecllist -> protocolname parameterdecllist roledecllist )
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == GLOBALKW) :
                    LA18_1 = self.input.LA(2)

                    if (LA18_1 == PROTOCOLKW) :
                        LA18_2 = self.input.LA(3)

                        if (LA18_2 == IDENTIFIER) :
                            LA18_3 = self.input.LA(4)

                            if (LA18_3 == 94) :
                                alt18 = 1
                            elif (LA18_3 == 100) :
                                alt18 = 2
                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                nvae = NoViableAltException("", 18, 3, self.input)

                                raise nvae


                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 18, 2, self.input)

                            raise nvae


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 18, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 18, 0, self.input)

                    raise nvae


                if alt18 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:395:2: GLOBALKW PROTOCOLKW protocolname roledecllist
                    pass 
                    GLOBALKW85 = self.match(self.input, GLOBALKW, self.FOLLOW_GLOBALKW_in_globalprotocolheader1775) 
                    if self._state.backtracking == 0:
                        stream_GLOBALKW.add(GLOBALKW85)


                    PROTOCOLKW86 = self.match(self.input, PROTOCOLKW, self.FOLLOW_PROTOCOLKW_in_globalprotocolheader1777) 
                    if self._state.backtracking == 0:
                        stream_PROTOCOLKW.add(PROTOCOLKW86)


                    self._state.following.append(self.FOLLOW_protocolname_in_globalprotocolheader1779)
                    protocolname87 = self.protocolname()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_protocolname.add(protocolname87.tree)


                    self._state.following.append(self.FOLLOW_roledecllist_in_globalprotocolheader1781)
                    roledecllist88 = self.roledecllist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roledecllist.add(roledecllist88.tree)


                    # AST Rewrite
                    # elements: protocolname, roledecllist
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 396:2: -> protocolname EMPTY_PARAMETER_DECL_LIST roledecllist
                        self._adaptor.addChild(root_0, stream_protocolname.nextTree())

                        self._adaptor.addChild(root_0, 
                        self._adaptor.createFromType(EMPTY_PARAMETER_DECL_LIST, "EMPTY_PARAMETER_DECL_LIST")
                        )

                        self._adaptor.addChild(root_0, stream_roledecllist.nextTree())




                        retval.tree = root_0




                elif alt18 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:399:2: GLOBALKW PROTOCOLKW protocolname parameterdecllist roledecllist
                    pass 
                    GLOBALKW89 = self.match(self.input, GLOBALKW, self.FOLLOW_GLOBALKW_in_globalprotocolheader1796) 
                    if self._state.backtracking == 0:
                        stream_GLOBALKW.add(GLOBALKW89)


                    PROTOCOLKW90 = self.match(self.input, PROTOCOLKW, self.FOLLOW_PROTOCOLKW_in_globalprotocolheader1798) 
                    if self._state.backtracking == 0:
                        stream_PROTOCOLKW.add(PROTOCOLKW90)


                    self._state.following.append(self.FOLLOW_protocolname_in_globalprotocolheader1800)
                    protocolname91 = self.protocolname()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_protocolname.add(protocolname91.tree)


                    self._state.following.append(self.FOLLOW_parameterdecllist_in_globalprotocolheader1802)
                    parameterdecllist92 = self.parameterdecllist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameterdecllist.add(parameterdecllist92.tree)


                    self._state.following.append(self.FOLLOW_roledecllist_in_globalprotocolheader1804)
                    roledecllist93 = self.roledecllist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roledecllist.add(roledecllist93.tree)


                    # AST Rewrite
                    # elements: protocolname, roledecllist, parameterdecllist
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 400:2: -> protocolname parameterdecllist roledecllist
                        self._adaptor.addChild(root_0, stream_protocolname.nextTree())

                        self._adaptor.addChild(root_0, stream_parameterdecllist.nextTree())

                        self._adaptor.addChild(root_0, stream_roledecllist.nextTree())




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "globalprotocolheader"


    class roledecllist_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "roledecllist"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:404:1: roledecllist : '(' roledecl ( ',' roledecl )* ')' -> ^( ROLEDECLLIST ( roledecl )+ ) ;
    def roledecllist(self, ):
        retval = self.roledecllist_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal94 = None
        char_literal96 = None
        char_literal98 = None
        roledecl95 = None
        roledecl97 = None

        char_literal94_tree = None
        char_literal96_tree = None
        char_literal98_tree = None
        stream_94 = RewriteRuleTokenStream(self._adaptor, "token 94")
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_96 = RewriteRuleTokenStream(self._adaptor, "token 96")
        stream_roledecl = RewriteRuleSubtreeStream(self._adaptor, "rule roledecl")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:404:13: ( '(' roledecl ( ',' roledecl )* ')' -> ^( ROLEDECLLIST ( roledecl )+ ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:405:2: '(' roledecl ( ',' roledecl )* ')'
                pass 
                char_literal94 = self.match(self.input, 94, self.FOLLOW_94_in_roledecllist1823) 
                if self._state.backtracking == 0:
                    stream_94.add(char_literal94)


                self._state.following.append(self.FOLLOW_roledecl_in_roledecllist1825)
                roledecl95 = self.roledecl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_roledecl.add(roledecl95.tree)


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:405:15: ( ',' roledecl )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == 96) :
                        alt19 = 1


                    if alt19 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:405:16: ',' roledecl
                        pass 
                        char_literal96 = self.match(self.input, 96, self.FOLLOW_96_in_roledecllist1828) 
                        if self._state.backtracking == 0:
                            stream_96.add(char_literal96)


                        self._state.following.append(self.FOLLOW_roledecl_in_roledecllist1830)
                        roledecl97 = self.roledecl()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_roledecl.add(roledecl97.tree)



                    else:
                        break #loop19


                char_literal98 = self.match(self.input, 95, self.FOLLOW_95_in_roledecllist1834) 
                if self._state.backtracking == 0:
                    stream_95.add(char_literal98)


                # AST Rewrite
                # elements: roledecl
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 406:2: -> ^( ROLEDECLLIST ( roledecl )+ )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:407:2: ^( ROLEDECLLIST ( roledecl )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(ROLEDECLLIST, "ROLEDECLLIST")
                    , root_1)

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:407:17: ( roledecl )+
                    if not (stream_roledecl.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_roledecl.hasNext():
                        self._adaptor.addChild(root_1, stream_roledecl.nextTree())


                    stream_roledecl.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "roledecllist"


    class roledecl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "roledecl"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:410:1: roledecl : ( ROLEKW rolename -> ^( ROLEDECL rolename ) | ROLEKW rolename ASKW rolename -> ^( ROLEDECL rolename rolename ) );
    def roledecl(self, ):
        retval = self.roledecl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ROLEKW99 = None
        ROLEKW101 = None
        ASKW103 = None
        rolename100 = None
        rolename102 = None
        rolename104 = None

        ROLEKW99_tree = None
        ROLEKW101_tree = None
        ASKW103_tree = None
        stream_ASKW = RewriteRuleTokenStream(self._adaptor, "token ASKW")
        stream_ROLEKW = RewriteRuleTokenStream(self._adaptor, "token ROLEKW")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:410:9: ( ROLEKW rolename -> ^( ROLEDECL rolename ) | ROLEKW rolename ASKW rolename -> ^( ROLEDECL rolename rolename ) )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == ROLEKW) :
                    LA20_1 = self.input.LA(2)

                    if (LA20_1 == IDENTIFIER) :
                        LA20_2 = self.input.LA(3)

                        if (LA20_2 in {EOF, 95, 96}) :
                            alt20 = 1
                        elif (LA20_2 == ASKW) :
                            alt20 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 20, 2, self.input)

                            raise nvae


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 20, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae


                if alt20 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:411:2: ROLEKW rolename
                    pass 
                    ROLEKW99 = self.match(self.input, ROLEKW, self.FOLLOW_ROLEKW_in_roledecl1856) 
                    if self._state.backtracking == 0:
                        stream_ROLEKW.add(ROLEKW99)


                    self._state.following.append(self.FOLLOW_rolename_in_roledecl1858)
                    rolename100 = self.rolename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_rolename.add(rolename100.tree)


                    # AST Rewrite
                    # elements: rolename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 412:2: -> ^( ROLEDECL rolename )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:413:2: ^( ROLEDECL rolename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(ROLEDECL, "ROLEDECL")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_rolename.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt20 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:415:2: ROLEKW rolename ASKW rolename
                    pass 
                    ROLEKW101 = self.match(self.input, ROLEKW, self.FOLLOW_ROLEKW_in_roledecl1873) 
                    if self._state.backtracking == 0:
                        stream_ROLEKW.add(ROLEKW101)


                    self._state.following.append(self.FOLLOW_rolename_in_roledecl1875)
                    rolename102 = self.rolename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_rolename.add(rolename102.tree)


                    ASKW103 = self.match(self.input, ASKW, self.FOLLOW_ASKW_in_roledecl1877) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW103)


                    self._state.following.append(self.FOLLOW_rolename_in_roledecl1879)
                    rolename104 = self.rolename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_rolename.add(rolename104.tree)


                    # AST Rewrite
                    # elements: rolename, rolename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 416:2: -> ^( ROLEDECL rolename rolename )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:417:2: ^( ROLEDECL rolename rolename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(ROLEDECL, "ROLEDECL")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_rolename.nextTree())

                        self._adaptor.addChild(root_1, stream_rolename.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "roledecl"


    class parameterdecllist_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "parameterdecllist"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:420:1: parameterdecllist : '<' parameterdecl ( ',' parameterdecl )* '>' -> ^( PARAMETERDECLLIST ( parameterdecl )+ ) ;
    def parameterdecllist(self, ):
        retval = self.parameterdecllist_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal105 = None
        char_literal107 = None
        char_literal109 = None
        parameterdecl106 = None
        parameterdecl108 = None

        char_literal105_tree = None
        char_literal107_tree = None
        char_literal109_tree = None
        stream_100 = RewriteRuleTokenStream(self._adaptor, "token 100")
        stream_101 = RewriteRuleTokenStream(self._adaptor, "token 101")
        stream_96 = RewriteRuleTokenStream(self._adaptor, "token 96")
        stream_parameterdecl = RewriteRuleSubtreeStream(self._adaptor, "rule parameterdecl")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:420:18: ( '<' parameterdecl ( ',' parameterdecl )* '>' -> ^( PARAMETERDECLLIST ( parameterdecl )+ ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:421:2: '<' parameterdecl ( ',' parameterdecl )* '>'
                pass 
                char_literal105 = self.match(self.input, 100, self.FOLLOW_100_in_parameterdecllist1900) 
                if self._state.backtracking == 0:
                    stream_100.add(char_literal105)


                self._state.following.append(self.FOLLOW_parameterdecl_in_parameterdecllist1902)
                parameterdecl106 = self.parameterdecl()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_parameterdecl.add(parameterdecl106.tree)


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:421:20: ( ',' parameterdecl )*
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == 96) :
                        alt21 = 1


                    if alt21 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:421:21: ',' parameterdecl
                        pass 
                        char_literal107 = self.match(self.input, 96, self.FOLLOW_96_in_parameterdecllist1905) 
                        if self._state.backtracking == 0:
                            stream_96.add(char_literal107)


                        self._state.following.append(self.FOLLOW_parameterdecl_in_parameterdecllist1907)
                        parameterdecl108 = self.parameterdecl()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_parameterdecl.add(parameterdecl108.tree)



                    else:
                        break #loop21


                char_literal109 = self.match(self.input, 101, self.FOLLOW_101_in_parameterdecllist1911) 
                if self._state.backtracking == 0:
                    stream_101.add(char_literal109)


                # AST Rewrite
                # elements: parameterdecl
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 422:2: -> ^( PARAMETERDECLLIST ( parameterdecl )+ )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:423:2: ^( PARAMETERDECLLIST ( parameterdecl )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(PARAMETERDECLLIST, "PARAMETERDECLLIST")
                    , root_1)

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:423:22: ( parameterdecl )+
                    if not (stream_parameterdecl.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_parameterdecl.hasNext():
                        self._adaptor.addChild(root_1, stream_parameterdecl.nextTree())


                    stream_parameterdecl.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "parameterdecllist"


    class parameterdecl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "parameterdecl"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:426:1: parameterdecl : ( TYPEKW parametername -> ^( PARAMETERDECL KIND_PAYLOAD_TYPE parametername ) | TYPEKW parametername ASKW parametername -> ^( PARAMETERDECL KIND_PAYLOAD_TYPE parametername parametername ) | SIGKW parametername -> ^( PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername ) | SIGKW parametername ASKW parametername -> ^( PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername parametername ) );
    def parameterdecl(self, ):
        retval = self.parameterdecl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TYPEKW110 = None
        TYPEKW112 = None
        ASKW114 = None
        SIGKW116 = None
        SIGKW118 = None
        ASKW120 = None
        parametername111 = None
        parametername113 = None
        parametername115 = None
        parametername117 = None
        parametername119 = None
        parametername121 = None

        TYPEKW110_tree = None
        TYPEKW112_tree = None
        ASKW114_tree = None
        SIGKW116_tree = None
        SIGKW118_tree = None
        ASKW120_tree = None
        stream_ASKW = RewriteRuleTokenStream(self._adaptor, "token ASKW")
        stream_TYPEKW = RewriteRuleTokenStream(self._adaptor, "token TYPEKW")
        stream_SIGKW = RewriteRuleTokenStream(self._adaptor, "token SIGKW")
        stream_parametername = RewriteRuleSubtreeStream(self._adaptor, "rule parametername")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:426:14: ( TYPEKW parametername -> ^( PARAMETERDECL KIND_PAYLOAD_TYPE parametername ) | TYPEKW parametername ASKW parametername -> ^( PARAMETERDECL KIND_PAYLOAD_TYPE parametername parametername ) | SIGKW parametername -> ^( PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername ) | SIGKW parametername ASKW parametername -> ^( PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername parametername ) )
                alt22 = 4
                LA22_0 = self.input.LA(1)

                if (LA22_0 == TYPEKW) :
                    LA22_1 = self.input.LA(2)

                    if (LA22_1 == IDENTIFIER) :
                        LA22_3 = self.input.LA(3)

                        if (LA22_3 in {EOF, 96, 101}) :
                            alt22 = 1
                        elif (LA22_3 == ASKW) :
                            alt22 = 2
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 22, 3, self.input)

                            raise nvae


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 22, 1, self.input)

                        raise nvae


                elif (LA22_0 == SIGKW) :
                    LA22_2 = self.input.LA(2)

                    if (LA22_2 == IDENTIFIER) :
                        LA22_4 = self.input.LA(3)

                        if (LA22_4 in {EOF, 96, 101}) :
                            alt22 = 3
                        elif (LA22_4 == ASKW) :
                            alt22 = 4
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 22, 4, self.input)

                            raise nvae


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 22, 2, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae


                if alt22 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:427:3: TYPEKW parametername
                    pass 
                    TYPEKW110 = self.match(self.input, TYPEKW, self.FOLLOW_TYPEKW_in_parameterdecl1934) 
                    if self._state.backtracking == 0:
                        stream_TYPEKW.add(TYPEKW110)


                    self._state.following.append(self.FOLLOW_parametername_in_parameterdecl1936)
                    parametername111 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername111.tree)


                    # AST Rewrite
                    # elements: parametername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 428:2: -> ^( PARAMETERDECL KIND_PAYLOAD_TYPE parametername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:429:2: ^( PARAMETERDECL KIND_PAYLOAD_TYPE parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(PARAMETERDECL, "PARAMETERDECL")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(KIND_PAYLOAD_TYPE, "KIND_PAYLOAD_TYPE")
                        )

                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt22 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:431:3: TYPEKW parametername ASKW parametername
                    pass 
                    TYPEKW112 = self.match(self.input, TYPEKW, self.FOLLOW_TYPEKW_in_parameterdecl1954) 
                    if self._state.backtracking == 0:
                        stream_TYPEKW.add(TYPEKW112)


                    self._state.following.append(self.FOLLOW_parametername_in_parameterdecl1956)
                    parametername113 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername113.tree)


                    ASKW114 = self.match(self.input, ASKW, self.FOLLOW_ASKW_in_parameterdecl1958) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW114)


                    self._state.following.append(self.FOLLOW_parametername_in_parameterdecl1960)
                    parametername115 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername115.tree)


                    # AST Rewrite
                    # elements: parametername, parametername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 432:2: -> ^( PARAMETERDECL KIND_PAYLOAD_TYPE parametername parametername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:433:2: ^( PARAMETERDECL KIND_PAYLOAD_TYPE parametername parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(PARAMETERDECL, "PARAMETERDECL")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(KIND_PAYLOAD_TYPE, "KIND_PAYLOAD_TYPE")
                        )

                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt22 == 3:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:435:3: SIGKW parametername
                    pass 
                    SIGKW116 = self.match(self.input, SIGKW, self.FOLLOW_SIGKW_in_parameterdecl1980) 
                    if self._state.backtracking == 0:
                        stream_SIGKW.add(SIGKW116)


                    self._state.following.append(self.FOLLOW_parametername_in_parameterdecl1982)
                    parametername117 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername117.tree)


                    # AST Rewrite
                    # elements: parametername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 436:2: -> ^( PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:437:2: ^( PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(PARAMETERDECL, "PARAMETERDECL")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(KIND_MESSAGE_SIGNATURE, "KIND_MESSAGE_SIGNATURE")
                        )

                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt22 == 4:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:439:3: SIGKW parametername ASKW parametername
                    pass 
                    SIGKW118 = self.match(self.input, SIGKW, self.FOLLOW_SIGKW_in_parameterdecl2000) 
                    if self._state.backtracking == 0:
                        stream_SIGKW.add(SIGKW118)


                    self._state.following.append(self.FOLLOW_parametername_in_parameterdecl2002)
                    parametername119 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername119.tree)


                    ASKW120 = self.match(self.input, ASKW, self.FOLLOW_ASKW_in_parameterdecl2004) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW120)


                    self._state.following.append(self.FOLLOW_parametername_in_parameterdecl2006)
                    parametername121 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername121.tree)


                    # AST Rewrite
                    # elements: parametername, parametername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 440:2: -> ^( PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername parametername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:441:2: ^( PARAMETERDECL KIND_MESSAGE_SIGNATURE parametername parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(PARAMETERDECL, "PARAMETERDECL")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(KIND_MESSAGE_SIGNATURE, "KIND_MESSAGE_SIGNATURE")
                        )

                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "parameterdecl"


    class globalprotocoldefinition_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "globalprotocoldefinition"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:448:1: globalprotocoldefinition : globalprotocolblock -> ^( GLOBALPROTOCOLDEF globalprotocolblock ) ;
    def globalprotocoldefinition(self, ):
        retval = self.globalprotocoldefinition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        globalprotocolblock122 = None

        stream_globalprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule globalprotocolblock")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:448:25: ( globalprotocolblock -> ^( GLOBALPROTOCOLDEF globalprotocolblock ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:449:2: globalprotocolblock
                pass 
                self._state.following.append(self.FOLLOW_globalprotocolblock_in_globalprotocoldefinition2032)
                globalprotocolblock122 = self.globalprotocolblock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_globalprotocolblock.add(globalprotocolblock122.tree)


                # AST Rewrite
                # elements: globalprotocolblock
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 450:2: -> ^( GLOBALPROTOCOLDEF globalprotocolblock )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:451:2: ^( GLOBALPROTOCOLDEF globalprotocolblock )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(GLOBALPROTOCOLDEF, "GLOBALPROTOCOLDEF")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_globalprotocolblock.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "globalprotocoldefinition"


    class globalprotocolinstance_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "globalprotocolinstance"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:458:1: globalprotocolinstance : ( INSTANTIATESKW membername roleinstantiationlist ';' -> ^( GLOBALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | INSTANTIATESKW membername argumentlist roleinstantiationlist ';' -> ^( GLOBALPROTOCOLINSTANCE argumentlist roleinstantiationlist membername ) );
    def globalprotocolinstance(self, ):
        retval = self.globalprotocolinstance_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INSTANTIATESKW123 = None
        char_literal126 = None
        INSTANTIATESKW127 = None
        char_literal131 = None
        membername124 = None
        roleinstantiationlist125 = None
        membername128 = None
        argumentlist129 = None
        roleinstantiationlist130 = None

        INSTANTIATESKW123_tree = None
        char_literal126_tree = None
        INSTANTIATESKW127_tree = None
        char_literal131_tree = None
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_INSTANTIATESKW = RewriteRuleTokenStream(self._adaptor, "token INSTANTIATESKW")
        stream_argumentlist = RewriteRuleSubtreeStream(self._adaptor, "rule argumentlist")
        stream_roleinstantiationlist = RewriteRuleSubtreeStream(self._adaptor, "rule roleinstantiationlist")
        stream_membername = RewriteRuleSubtreeStream(self._adaptor, "rule membername")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:458:23: ( INSTANTIATESKW membername roleinstantiationlist ';' -> ^( GLOBALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | INSTANTIATESKW membername argumentlist roleinstantiationlist ';' -> ^( GLOBALPROTOCOLINSTANCE argumentlist roleinstantiationlist membername ) )
                alt23 = 2
                alt23 = self.dfa23.predict(self.input)
                if alt23 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:459:2: INSTANTIATESKW membername roleinstantiationlist ';'
                    pass 
                    INSTANTIATESKW123 = self.match(self.input, INSTANTIATESKW, self.FOLLOW_INSTANTIATESKW_in_globalprotocolinstance2054) 
                    if self._state.backtracking == 0:
                        stream_INSTANTIATESKW.add(INSTANTIATESKW123)


                    self._state.following.append(self.FOLLOW_membername_in_globalprotocolinstance2056)
                    membername124 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername124.tree)


                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_globalprotocolinstance2058)
                    roleinstantiationlist125 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist125.tree)


                    char_literal126 = self.match(self.input, 99, self.FOLLOW_99_in_globalprotocolinstance2060) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal126)


                    # AST Rewrite
                    # elements: membername, roleinstantiationlist
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 460:2: -> ^( GLOBALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:461:2: ^( GLOBALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(GLOBALPROTOCOLINSTANCE, "GLOBALPROTOCOLINSTANCE")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(EMPTY_ARGUMENT_LIST, "EMPTY_ARGUMENT_LIST")
                        )

                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())

                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt23 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:464:2: INSTANTIATESKW membername argumentlist roleinstantiationlist ';'
                    pass 
                    INSTANTIATESKW127 = self.match(self.input, INSTANTIATESKW, self.FOLLOW_INSTANTIATESKW_in_globalprotocolinstance2081) 
                    if self._state.backtracking == 0:
                        stream_INSTANTIATESKW.add(INSTANTIATESKW127)


                    self._state.following.append(self.FOLLOW_membername_in_globalprotocolinstance2083)
                    membername128 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername128.tree)


                    self._state.following.append(self.FOLLOW_argumentlist_in_globalprotocolinstance2085)
                    argumentlist129 = self.argumentlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_argumentlist.add(argumentlist129.tree)


                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_globalprotocolinstance2087)
                    roleinstantiationlist130 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist130.tree)


                    char_literal131 = self.match(self.input, 99, self.FOLLOW_99_in_globalprotocolinstance2089) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal131)


                    # AST Rewrite
                    # elements: roleinstantiationlist, argumentlist, membername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 465:2: -> ^( GLOBALPROTOCOLINSTANCE argumentlist roleinstantiationlist membername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:466:2: ^( GLOBALPROTOCOLINSTANCE argumentlist roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(GLOBALPROTOCOLINSTANCE, "GLOBALPROTOCOLINSTANCE")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_argumentlist.nextTree())

                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())

                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "globalprotocolinstance"


    class roleinstantiationlist_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "roleinstantiationlist"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:469:1: roleinstantiationlist : '(' roleinstantiation ( ',' roleinstantiation )* ')' -> ^( ROLEINSTANTIATIONLIST ( roleinstantiation )+ ) ;
    def roleinstantiationlist(self, ):
        retval = self.roleinstantiationlist_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal132 = None
        char_literal134 = None
        char_literal136 = None
        roleinstantiation133 = None
        roleinstantiation135 = None

        char_literal132_tree = None
        char_literal134_tree = None
        char_literal136_tree = None
        stream_94 = RewriteRuleTokenStream(self._adaptor, "token 94")
        stream_95 = RewriteRuleTokenStream(self._adaptor, "token 95")
        stream_96 = RewriteRuleTokenStream(self._adaptor, "token 96")
        stream_roleinstantiation = RewriteRuleSubtreeStream(self._adaptor, "rule roleinstantiation")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:469:22: ( '(' roleinstantiation ( ',' roleinstantiation )* ')' -> ^( ROLEINSTANTIATIONLIST ( roleinstantiation )+ ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:470:2: '(' roleinstantiation ( ',' roleinstantiation )* ')'
                pass 
                char_literal132 = self.match(self.input, 94, self.FOLLOW_94_in_roleinstantiationlist2112) 
                if self._state.backtracking == 0:
                    stream_94.add(char_literal132)


                self._state.following.append(self.FOLLOW_roleinstantiation_in_roleinstantiationlist2114)
                roleinstantiation133 = self.roleinstantiation()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_roleinstantiation.add(roleinstantiation133.tree)


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:470:24: ( ',' roleinstantiation )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == 96) :
                        alt24 = 1


                    if alt24 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:470:25: ',' roleinstantiation
                        pass 
                        char_literal134 = self.match(self.input, 96, self.FOLLOW_96_in_roleinstantiationlist2117) 
                        if self._state.backtracking == 0:
                            stream_96.add(char_literal134)


                        self._state.following.append(self.FOLLOW_roleinstantiation_in_roleinstantiationlist2119)
                        roleinstantiation135 = self.roleinstantiation()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_roleinstantiation.add(roleinstantiation135.tree)



                    else:
                        break #loop24


                char_literal136 = self.match(self.input, 95, self.FOLLOW_95_in_roleinstantiationlist2123) 
                if self._state.backtracking == 0:
                    stream_95.add(char_literal136)


                # AST Rewrite
                # elements: roleinstantiation
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 471:2: -> ^( ROLEINSTANTIATIONLIST ( roleinstantiation )+ )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:472:2: ^( ROLEINSTANTIATIONLIST ( roleinstantiation )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(ROLEINSTANTIATIONLIST, "ROLEINSTANTIATIONLIST")
                    , root_1)

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:472:26: ( roleinstantiation )+
                    if not (stream_roleinstantiation.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_roleinstantiation.hasNext():
                        self._adaptor.addChild(root_1, stream_roleinstantiation.nextTree())


                    stream_roleinstantiation.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "roleinstantiationlist"


    class roleinstantiation_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "roleinstantiation"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:475:1: roleinstantiation : ( rolename -> ^( ROLEINSTANTIATION rolename ) | rolename ASKW rolename -> ^( ROLEINSTANTIATION rolename rolename ) );
    def roleinstantiation(self, ):
        retval = self.roleinstantiation_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ASKW139 = None
        rolename137 = None
        rolename138 = None
        rolename140 = None

        ASKW139_tree = None
        stream_ASKW = RewriteRuleTokenStream(self._adaptor, "token ASKW")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:475:18: ( rolename -> ^( ROLEINSTANTIATION rolename ) | rolename ASKW rolename -> ^( ROLEINSTANTIATION rolename rolename ) )
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == IDENTIFIER) :
                    LA25_1 = self.input.LA(2)

                    if (LA25_1 in {EOF, 95, 96}) :
                        alt25 = 1
                    elif (LA25_1 == ASKW) :
                        alt25 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 25, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae


                if alt25 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:476:2: rolename
                    pass 
                    self._state.following.append(self.FOLLOW_rolename_in_roleinstantiation2145)
                    rolename137 = self.rolename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_rolename.add(rolename137.tree)


                    # AST Rewrite
                    # elements: rolename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 477:2: -> ^( ROLEINSTANTIATION rolename )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:478:2: ^( ROLEINSTANTIATION rolename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(ROLEINSTANTIATION, "ROLEINSTANTIATION")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_rolename.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt25 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:480:2: rolename ASKW rolename
                    pass 
                    self._state.following.append(self.FOLLOW_rolename_in_roleinstantiation2160)
                    rolename138 = self.rolename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_rolename.add(rolename138.tree)


                    ASKW139 = self.match(self.input, ASKW, self.FOLLOW_ASKW_in_roleinstantiation2162) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW139)


                    self._state.following.append(self.FOLLOW_rolename_in_roleinstantiation2164)
                    rolename140 = self.rolename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_rolename.add(rolename140.tree)


                    # AST Rewrite
                    # elements: rolename, rolename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 481:2: -> ^( ROLEINSTANTIATION rolename rolename )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:482:2: ^( ROLEINSTANTIATION rolename rolename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(ROLEINSTANTIATION, "ROLEINSTANTIATION")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_rolename.nextTree())

                        self._adaptor.addChild(root_1, stream_rolename.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "roleinstantiation"


    class argumentlist_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "argumentlist"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:485:1: argumentlist : '<' argument ( ',' argument )* '>' -> ^( ARGUMENTLIST ( argument )+ ) ;
    def argumentlist(self, ):
        retval = self.argumentlist_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal141 = None
        char_literal143 = None
        char_literal145 = None
        argument142 = None
        argument144 = None

        char_literal141_tree = None
        char_literal143_tree = None
        char_literal145_tree = None
        stream_100 = RewriteRuleTokenStream(self._adaptor, "token 100")
        stream_101 = RewriteRuleTokenStream(self._adaptor, "token 101")
        stream_96 = RewriteRuleTokenStream(self._adaptor, "token 96")
        stream_argument = RewriteRuleSubtreeStream(self._adaptor, "rule argument")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:485:13: ( '<' argument ( ',' argument )* '>' -> ^( ARGUMENTLIST ( argument )+ ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:486:2: '<' argument ( ',' argument )* '>'
                pass 
                char_literal141 = self.match(self.input, 100, self.FOLLOW_100_in_argumentlist2185) 
                if self._state.backtracking == 0:
                    stream_100.add(char_literal141)


                self._state.following.append(self.FOLLOW_argument_in_argumentlist2187)
                argument142 = self.argument()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_argument.add(argument142.tree)


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:486:15: ( ',' argument )*
                while True: #loop26
                    alt26 = 2
                    LA26_0 = self.input.LA(1)

                    if (LA26_0 == 96) :
                        alt26 = 1


                    if alt26 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:486:16: ',' argument
                        pass 
                        char_literal143 = self.match(self.input, 96, self.FOLLOW_96_in_argumentlist2190) 
                        if self._state.backtracking == 0:
                            stream_96.add(char_literal143)


                        self._state.following.append(self.FOLLOW_argument_in_argumentlist2192)
                        argument144 = self.argument()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_argument.add(argument144.tree)



                    else:
                        break #loop26


                char_literal145 = self.match(self.input, 101, self.FOLLOW_101_in_argumentlist2196) 
                if self._state.backtracking == 0:
                    stream_101.add(char_literal145)


                # AST Rewrite
                # elements: argument
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 487:2: -> ^( ARGUMENTLIST ( argument )+ )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:488:2: ^( ARGUMENTLIST ( argument )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(ARGUMENTLIST, "ARGUMENTLIST")
                    , root_1)

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:488:17: ( argument )+
                    if not (stream_argument.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_argument.hasNext():
                        self._adaptor.addChild(root_1, stream_argument.nextTree())


                    stream_argument.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "argumentlist"


    class argument_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "argument"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:491:1: argument : ( messagesignature -> ^( ARGUMENT messagesignature ) | messagesignature ASKW parametername -> ^( ARGUMENT messagesignature parametername ) | payloadtypename -> ^( ARGUMENT payloadtypename ) | payloadtypename ASKW parametername -> ^( ARGUMENT payloadtypename parametername ) | parametername -> ^( ARGUMENT parametername ) | parametername ASKW parametername -> ^( ARGUMENT parametername ASKW parametername ) );
    def argument(self, ):
        retval = self.argument_return()
        retval.start = self.input.LT(1)


        root_0 = None

        ASKW148 = None
        ASKW152 = None
        ASKW156 = None
        messagesignature146 = None
        messagesignature147 = None
        parametername149 = None
        payloadtypename150 = None
        payloadtypename151 = None
        parametername153 = None
        parametername154 = None
        parametername155 = None
        parametername157 = None

        ASKW148_tree = None
        ASKW152_tree = None
        ASKW156_tree = None
        stream_ASKW = RewriteRuleTokenStream(self._adaptor, "token ASKW")
        stream_messagesignature = RewriteRuleSubtreeStream(self._adaptor, "rule messagesignature")
        stream_parametername = RewriteRuleSubtreeStream(self._adaptor, "rule parametername")
        stream_payloadtypename = RewriteRuleSubtreeStream(self._adaptor, "rule payloadtypename")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:491:9: ( messagesignature -> ^( ARGUMENT messagesignature ) | messagesignature ASKW parametername -> ^( ARGUMENT messagesignature parametername ) | payloadtypename -> ^( ARGUMENT payloadtypename ) | payloadtypename ASKW parametername -> ^( ARGUMENT payloadtypename parametername ) | parametername -> ^( ARGUMENT parametername ) | parametername ASKW parametername -> ^( ARGUMENT parametername ASKW parametername ) )
                alt27 = 6
                alt27 = self.dfa27.predict(self.input)
                if alt27 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:492:2: messagesignature
                    pass 
                    self._state.following.append(self.FOLLOW_messagesignature_in_argument2218)
                    messagesignature146 = self.messagesignature()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_messagesignature.add(messagesignature146.tree)


                    # AST Rewrite
                    # elements: messagesignature
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 493:2: -> ^( ARGUMENT messagesignature )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:494:2: ^( ARGUMENT messagesignature )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(ARGUMENT, "ARGUMENT")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_messagesignature.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt27 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:496:2: messagesignature ASKW parametername
                    pass 
                    self._state.following.append(self.FOLLOW_messagesignature_in_argument2233)
                    messagesignature147 = self.messagesignature()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_messagesignature.add(messagesignature147.tree)


                    ASKW148 = self.match(self.input, ASKW, self.FOLLOW_ASKW_in_argument2235) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW148)


                    self._state.following.append(self.FOLLOW_parametername_in_argument2237)
                    parametername149 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername149.tree)


                    # AST Rewrite
                    # elements: parametername, messagesignature
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 497:2: -> ^( ARGUMENT messagesignature parametername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:498:2: ^( ARGUMENT messagesignature parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(ARGUMENT, "ARGUMENT")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_messagesignature.nextTree())

                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt27 == 3:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:500:2: payloadtypename
                    pass 
                    self._state.following.append(self.FOLLOW_payloadtypename_in_argument2254)
                    payloadtypename150 = self.payloadtypename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_payloadtypename.add(payloadtypename150.tree)


                    # AST Rewrite
                    # elements: payloadtypename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 501:2: -> ^( ARGUMENT payloadtypename )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:502:2: ^( ARGUMENT payloadtypename )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(ARGUMENT, "ARGUMENT")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_payloadtypename.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt27 == 4:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:504:2: payloadtypename ASKW parametername
                    pass 
                    self._state.following.append(self.FOLLOW_payloadtypename_in_argument2269)
                    payloadtypename151 = self.payloadtypename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_payloadtypename.add(payloadtypename151.tree)


                    ASKW152 = self.match(self.input, ASKW, self.FOLLOW_ASKW_in_argument2271) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW152)


                    self._state.following.append(self.FOLLOW_parametername_in_argument2273)
                    parametername153 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername153.tree)


                    # AST Rewrite
                    # elements: payloadtypename, parametername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 505:2: -> ^( ARGUMENT payloadtypename parametername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:506:2: ^( ARGUMENT payloadtypename parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(ARGUMENT, "ARGUMENT")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_payloadtypename.nextTree())

                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt27 == 5:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:508:2: parametername
                    pass 
                    self._state.following.append(self.FOLLOW_parametername_in_argument2290)
                    parametername154 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername154.tree)


                    # AST Rewrite
                    # elements: parametername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 509:2: -> ^( ARGUMENT parametername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:510:2: ^( ARGUMENT parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(ARGUMENT, "ARGUMENT")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt27 == 6:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:512:2: parametername ASKW parametername
                    pass 
                    self._state.following.append(self.FOLLOW_parametername_in_argument2307)
                    parametername155 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername155.tree)


                    ASKW156 = self.match(self.input, ASKW, self.FOLLOW_ASKW_in_argument2309) 
                    if self._state.backtracking == 0:
                        stream_ASKW.add(ASKW156)


                    self._state.following.append(self.FOLLOW_parametername_in_argument2311)
                    parametername157 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parametername.add(parametername157.tree)


                    # AST Rewrite
                    # elements: parametername, parametername, ASKW
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 513:2: -> ^( ARGUMENT parametername ASKW parametername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:514:2: ^( ARGUMENT parametername ASKW parametername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(ARGUMENT, "ARGUMENT")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_1, 
                        stream_ASKW.nextNode()
                        )

                        self._adaptor.addChild(root_1, stream_parametername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "argument"


    class globalprotocolblock_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "globalprotocolblock"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:521:1: globalprotocolblock : '{' globalinteractionsequence '}' -> ^( GLOBALPROTOCOLBLOCK globalinteractionsequence ) ;
    def globalprotocolblock(self, ):
        retval = self.globalprotocolblock_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal158 = None
        char_literal160 = None
        globalinteractionsequence159 = None

        char_literal158_tree = None
        char_literal160_tree = None
        stream_102 = RewriteRuleTokenStream(self._adaptor, "token 102")
        stream_103 = RewriteRuleTokenStream(self._adaptor, "token 103")
        stream_globalinteractionsequence = RewriteRuleSubtreeStream(self._adaptor, "rule globalinteractionsequence")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:521:20: ( '{' globalinteractionsequence '}' -> ^( GLOBALPROTOCOLBLOCK globalinteractionsequence ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:522:2: '{' globalinteractionsequence '}'
                pass 
                char_literal158 = self.match(self.input, 102, self.FOLLOW_102_in_globalprotocolblock2337) 
                if self._state.backtracking == 0:
                    stream_102.add(char_literal158)


                self._state.following.append(self.FOLLOW_globalinteractionsequence_in_globalprotocolblock2339)
                globalinteractionsequence159 = self.globalinteractionsequence()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_globalinteractionsequence.add(globalinteractionsequence159.tree)


                char_literal160 = self.match(self.input, 103, self.FOLLOW_103_in_globalprotocolblock2341) 
                if self._state.backtracking == 0:
                    stream_103.add(char_literal160)


                # AST Rewrite
                # elements: globalinteractionsequence
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 523:2: -> ^( GLOBALPROTOCOLBLOCK globalinteractionsequence )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:524:2: ^( GLOBALPROTOCOLBLOCK globalinteractionsequence )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(GLOBALPROTOCOLBLOCK, "GLOBALPROTOCOLBLOCK")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_globalinteractionsequence.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "globalprotocolblock"


    class globalinteractionsequence_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "globalinteractionsequence"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:527:1: globalinteractionsequence : ( globalinteraction )* -> ^( GLOBALINTERACTIONSEQUENCE ( globalinteraction )* ) ;
    def globalinteractionsequence(self, ):
        retval = self.globalinteractionsequence_return()
        retval.start = self.input.LT(1)


        root_0 = None

        globalinteraction161 = None

        stream_globalinteraction = RewriteRuleSubtreeStream(self._adaptor, "rule globalinteraction")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:527:26: ( ( globalinteraction )* -> ^( GLOBALINTERACTIONSEQUENCE ( globalinteraction )* ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:528:2: ( globalinteraction )*
                pass 
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:528:2: ( globalinteraction )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 in {CHOICEKW, CONTINUEKW, DOKW, IDENTIFIER, INTERRUPTIBLEKW, PARKW, RECKW, 94}) :
                        alt28 = 1


                    if alt28 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:528:3: globalinteraction
                        pass 
                        self._state.following.append(self.FOLLOW_globalinteraction_in_globalinteractionsequence2361)
                        globalinteraction161 = self.globalinteraction()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_globalinteraction.add(globalinteraction161.tree)



                    else:
                        break #loop28


                # AST Rewrite
                # elements: globalinteraction
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 529:2: -> ^( GLOBALINTERACTIONSEQUENCE ( globalinteraction )* )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:530:2: ^( GLOBALINTERACTIONSEQUENCE ( globalinteraction )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(GLOBALINTERACTIONSEQUENCE, "GLOBALINTERACTIONSEQUENCE")
                    , root_1)

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:530:30: ( globalinteraction )*
                    while stream_globalinteraction.hasNext():
                        self._adaptor.addChild(root_1, stream_globalinteraction.nextTree())


                    stream_globalinteraction.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "globalinteractionsequence"


    class globalinteraction_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "globalinteraction"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:533:1: globalinteraction : ( globalmessagetransfer | globalchoice | globalrecursion | globalcontinue | globalparallel | globalinterruptible | globaldo );
    def globalinteraction(self, ):
        retval = self.globalinteraction_return()
        retval.start = self.input.LT(1)


        root_0 = None

        globalmessagetransfer162 = None
        globalchoice163 = None
        globalrecursion164 = None
        globalcontinue165 = None
        globalparallel166 = None
        globalinterruptible167 = None
        globaldo168 = None


        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:533:18: ( globalmessagetransfer | globalchoice | globalrecursion | globalcontinue | globalparallel | globalinterruptible | globaldo )
                alt29 = 7
                LA29 = self.input.LA(1)
                if LA29 in {IDENTIFIER, 94}:
                    alt29 = 1
                elif LA29 in {CHOICEKW}:
                    alt29 = 2
                elif LA29 in {RECKW}:
                    alt29 = 3
                elif LA29 in {CONTINUEKW}:
                    alt29 = 4
                elif LA29 in {PARKW}:
                    alt29 = 5
                elif LA29 in {INTERRUPTIBLEKW}:
                    alt29 = 6
                elif LA29 in {DOKW}:
                    alt29 = 7
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae


                if alt29 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:534:2: globalmessagetransfer
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_globalmessagetransfer_in_globalinteraction2385)
                    globalmessagetransfer162 = self.globalmessagetransfer()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, globalmessagetransfer162.tree)



                elif alt29 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:536:2: globalchoice
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_globalchoice_in_globalinteraction2390)
                    globalchoice163 = self.globalchoice()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, globalchoice163.tree)



                elif alt29 == 3:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:538:2: globalrecursion
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_globalrecursion_in_globalinteraction2395)
                    globalrecursion164 = self.globalrecursion()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, globalrecursion164.tree)



                elif alt29 == 4:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:540:2: globalcontinue
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_globalcontinue_in_globalinteraction2400)
                    globalcontinue165 = self.globalcontinue()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, globalcontinue165.tree)



                elif alt29 == 5:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:542:2: globalparallel
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_globalparallel_in_globalinteraction2405)
                    globalparallel166 = self.globalparallel()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, globalparallel166.tree)



                elif alt29 == 6:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:544:2: globalinterruptible
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_globalinterruptible_in_globalinteraction2410)
                    globalinterruptible167 = self.globalinterruptible()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, globalinterruptible167.tree)



                elif alt29 == 7:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:546:2: globaldo
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_globaldo_in_globalinteraction2415)
                    globaldo168 = self.globaldo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, globaldo168.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "globalinteraction"


    class globalmessagetransfer_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "globalmessagetransfer"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:555:1: globalmessagetransfer : message FROMKW rolename TOKW rolename ( ',' rolename )* ';' -> ^( GLOBALMESSAGETRANSFER message rolename ( rolename )+ ) ;
    def globalmessagetransfer(self, ):
        retval = self.globalmessagetransfer_return()
        retval.start = self.input.LT(1)


        root_0 = None

        FROMKW170 = None
        TOKW172 = None
        char_literal174 = None
        char_literal176 = None
        message169 = None
        rolename171 = None
        rolename173 = None
        rolename175 = None

        FROMKW170_tree = None
        TOKW172_tree = None
        char_literal174_tree = None
        char_literal176_tree = None
        stream_TOKW = RewriteRuleTokenStream(self._adaptor, "token TOKW")
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_96 = RewriteRuleTokenStream(self._adaptor, "token 96")
        stream_FROMKW = RewriteRuleTokenStream(self._adaptor, "token FROMKW")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        stream_message = RewriteRuleSubtreeStream(self._adaptor, "rule message")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:555:22: ( message FROMKW rolename TOKW rolename ( ',' rolename )* ';' -> ^( GLOBALMESSAGETRANSFER message rolename ( rolename )+ ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:556:2: message FROMKW rolename TOKW rolename ( ',' rolename )* ';'
                pass 
                self._state.following.append(self.FOLLOW_message_in_globalmessagetransfer2429)
                message169 = self.message()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_message.add(message169.tree)


                FROMKW170 = self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_globalmessagetransfer2431) 
                if self._state.backtracking == 0:
                    stream_FROMKW.add(FROMKW170)


                self._state.following.append(self.FOLLOW_rolename_in_globalmessagetransfer2433)
                rolename171 = self.rolename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rolename.add(rolename171.tree)


                TOKW172 = self.match(self.input, TOKW, self.FOLLOW_TOKW_in_globalmessagetransfer2435) 
                if self._state.backtracking == 0:
                    stream_TOKW.add(TOKW172)


                self._state.following.append(self.FOLLOW_rolename_in_globalmessagetransfer2437)
                rolename173 = self.rolename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rolename.add(rolename173.tree)


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:556:40: ( ',' rolename )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == 96) :
                        alt30 = 1


                    if alt30 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:556:41: ',' rolename
                        pass 
                        char_literal174 = self.match(self.input, 96, self.FOLLOW_96_in_globalmessagetransfer2440) 
                        if self._state.backtracking == 0:
                            stream_96.add(char_literal174)


                        self._state.following.append(self.FOLLOW_rolename_in_globalmessagetransfer2442)
                        rolename175 = self.rolename()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_rolename.add(rolename175.tree)



                    else:
                        break #loop30


                char_literal176 = self.match(self.input, 99, self.FOLLOW_99_in_globalmessagetransfer2447) 
                if self._state.backtracking == 0:
                    stream_99.add(char_literal176)


                # AST Rewrite
                # elements: message, rolename, rolename
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 557:2: -> ^( GLOBALMESSAGETRANSFER message rolename ( rolename )+ )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:558:2: ^( GLOBALMESSAGETRANSFER message rolename ( rolename )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(GLOBALMESSAGETRANSFER, "GLOBALMESSAGETRANSFER")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_message.nextTree())

                    self._adaptor.addChild(root_1, stream_rolename.nextTree())

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:558:43: ( rolename )+
                    if not (stream_rolename.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_rolename.hasNext():
                        self._adaptor.addChild(root_1, stream_rolename.nextTree())


                    stream_rolename.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "globalmessagetransfer"


    class message_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "message"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:561:1: message : ( messagesignature | parametername );
    def message(self, ):
        retval = self.message_return()
        retval.start = self.input.LT(1)


        root_0 = None

        messagesignature177 = None
        parametername178 = None


        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:561:8: ( messagesignature | parametername )
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == 94) :
                    alt31 = 1
                elif (LA31_0 == IDENTIFIER) :
                    LA31_2 = self.input.LA(2)

                    if (LA31_2 == 94) :
                        alt31 = 1
                    elif (LA31_2 in {EOF, BYKW, FROMKW, TOKW, 96}) :
                        alt31 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 31, 2, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae


                if alt31 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:562:2: messagesignature
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_messagesignature_in_message2473)
                    messagesignature177 = self.messagesignature()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, messagesignature177.tree)



                elif alt31 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:564:2: parametername
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_parametername_in_message2478)
                    parametername178 = self.parametername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, parametername178.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "message"


    class globalchoice_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "globalchoice"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:571:1: globalchoice : CHOICEKW ATKW rolename globalprotocolblock ( ORKW globalprotocolblock )* -> ^( GLOBALCHOICE rolename ( globalprotocolblock )+ ) ;
    def globalchoice(self, ):
        retval = self.globalchoice_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CHOICEKW179 = None
        ATKW180 = None
        ORKW183 = None
        rolename181 = None
        globalprotocolblock182 = None
        globalprotocolblock184 = None

        CHOICEKW179_tree = None
        ATKW180_tree = None
        ORKW183_tree = None
        stream_ATKW = RewriteRuleTokenStream(self._adaptor, "token ATKW")
        stream_ORKW = RewriteRuleTokenStream(self._adaptor, "token ORKW")
        stream_CHOICEKW = RewriteRuleTokenStream(self._adaptor, "token CHOICEKW")
        stream_globalprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule globalprotocolblock")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:571:13: ( CHOICEKW ATKW rolename globalprotocolblock ( ORKW globalprotocolblock )* -> ^( GLOBALCHOICE rolename ( globalprotocolblock )+ ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:572:2: CHOICEKW ATKW rolename globalprotocolblock ( ORKW globalprotocolblock )*
                pass 
                CHOICEKW179 = self.match(self.input, CHOICEKW, self.FOLLOW_CHOICEKW_in_globalchoice2490) 
                if self._state.backtracking == 0:
                    stream_CHOICEKW.add(CHOICEKW179)


                ATKW180 = self.match(self.input, ATKW, self.FOLLOW_ATKW_in_globalchoice2492) 
                if self._state.backtracking == 0:
                    stream_ATKW.add(ATKW180)


                self._state.following.append(self.FOLLOW_rolename_in_globalchoice2494)
                rolename181 = self.rolename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rolename.add(rolename181.tree)


                self._state.following.append(self.FOLLOW_globalprotocolblock_in_globalchoice2496)
                globalprotocolblock182 = self.globalprotocolblock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_globalprotocolblock.add(globalprotocolblock182.tree)


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:572:45: ( ORKW globalprotocolblock )*
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == ORKW) :
                        alt32 = 1


                    if alt32 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:572:46: ORKW globalprotocolblock
                        pass 
                        ORKW183 = self.match(self.input, ORKW, self.FOLLOW_ORKW_in_globalchoice2499) 
                        if self._state.backtracking == 0:
                            stream_ORKW.add(ORKW183)


                        self._state.following.append(self.FOLLOW_globalprotocolblock_in_globalchoice2501)
                        globalprotocolblock184 = self.globalprotocolblock()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_globalprotocolblock.add(globalprotocolblock184.tree)



                    else:
                        break #loop32


                # AST Rewrite
                # elements: globalprotocolblock, rolename
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 573:2: -> ^( GLOBALCHOICE rolename ( globalprotocolblock )+ )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:574:2: ^( GLOBALCHOICE rolename ( globalprotocolblock )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(GLOBALCHOICE, "GLOBALCHOICE")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_rolename.nextTree())

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:574:26: ( globalprotocolblock )+
                    if not (stream_globalprotocolblock.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_globalprotocolblock.hasNext():
                        self._adaptor.addChild(root_1, stream_globalprotocolblock.nextTree())


                    stream_globalprotocolblock.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "globalchoice"


    class globalrecursion_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "globalrecursion"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:581:1: globalrecursion : RECKW recursionlabelname globalprotocolblock -> ^( GLOBALRECURSION recursionlabelname globalprotocolblock ) ;
    def globalrecursion(self, ):
        retval = self.globalrecursion_return()
        retval.start = self.input.LT(1)


        root_0 = None

        RECKW185 = None
        recursionlabelname186 = None
        globalprotocolblock187 = None

        RECKW185_tree = None
        stream_RECKW = RewriteRuleTokenStream(self._adaptor, "token RECKW")
        stream_globalprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule globalprotocolblock")
        stream_recursionlabelname = RewriteRuleSubtreeStream(self._adaptor, "rule recursionlabelname")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:581:16: ( RECKW recursionlabelname globalprotocolblock -> ^( GLOBALRECURSION recursionlabelname globalprotocolblock ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:582:2: RECKW recursionlabelname globalprotocolblock
                pass 
                RECKW185 = self.match(self.input, RECKW, self.FOLLOW_RECKW_in_globalrecursion2528) 
                if self._state.backtracking == 0:
                    stream_RECKW.add(RECKW185)


                self._state.following.append(self.FOLLOW_recursionlabelname_in_globalrecursion2530)
                recursionlabelname186 = self.recursionlabelname()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_recursionlabelname.add(recursionlabelname186.tree)


                self._state.following.append(self.FOLLOW_globalprotocolblock_in_globalrecursion2532)
                globalprotocolblock187 = self.globalprotocolblock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_globalprotocolblock.add(globalprotocolblock187.tree)


                # AST Rewrite
                # elements: globalprotocolblock, recursionlabelname
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 583:2: -> ^( GLOBALRECURSION recursionlabelname globalprotocolblock )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:584:2: ^( GLOBALRECURSION recursionlabelname globalprotocolblock )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(GLOBALRECURSION, "GLOBALRECURSION")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_recursionlabelname.nextTree())

                    self._adaptor.addChild(root_1, stream_globalprotocolblock.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "globalrecursion"


    class globalcontinue_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "globalcontinue"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:587:1: globalcontinue : CONTINUEKW recursionlabelname ';' -> ^( GLOBALCONTINUE recursionlabelname ) ;
    def globalcontinue(self, ):
        retval = self.globalcontinue_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONTINUEKW188 = None
        char_literal190 = None
        recursionlabelname189 = None

        CONTINUEKW188_tree = None
        char_literal190_tree = None
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_CONTINUEKW = RewriteRuleTokenStream(self._adaptor, "token CONTINUEKW")
        stream_recursionlabelname = RewriteRuleSubtreeStream(self._adaptor, "rule recursionlabelname")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:587:15: ( CONTINUEKW recursionlabelname ';' -> ^( GLOBALCONTINUE recursionlabelname ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:588:2: CONTINUEKW recursionlabelname ';'
                pass 
                CONTINUEKW188 = self.match(self.input, CONTINUEKW, self.FOLLOW_CONTINUEKW_in_globalcontinue2553) 
                if self._state.backtracking == 0:
                    stream_CONTINUEKW.add(CONTINUEKW188)


                self._state.following.append(self.FOLLOW_recursionlabelname_in_globalcontinue2555)
                recursionlabelname189 = self.recursionlabelname()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_recursionlabelname.add(recursionlabelname189.tree)


                char_literal190 = self.match(self.input, 99, self.FOLLOW_99_in_globalcontinue2557) 
                if self._state.backtracking == 0:
                    stream_99.add(char_literal190)


                # AST Rewrite
                # elements: recursionlabelname
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 589:2: -> ^( GLOBALCONTINUE recursionlabelname )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:590:2: ^( GLOBALCONTINUE recursionlabelname )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(GLOBALCONTINUE, "GLOBALCONTINUE")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_recursionlabelname.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "globalcontinue"


    class globalparallel_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "globalparallel"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:597:1: globalparallel : PARKW globalprotocolblock ( ANDKW globalprotocolblock )* -> ^( GLOBALPARALLEL ( globalprotocolblock )+ ) ;
    def globalparallel(self, ):
        retval = self.globalparallel_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PARKW191 = None
        ANDKW193 = None
        globalprotocolblock192 = None
        globalprotocolblock194 = None

        PARKW191_tree = None
        ANDKW193_tree = None
        stream_PARKW = RewriteRuleTokenStream(self._adaptor, "token PARKW")
        stream_ANDKW = RewriteRuleTokenStream(self._adaptor, "token ANDKW")
        stream_globalprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule globalprotocolblock")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:597:15: ( PARKW globalprotocolblock ( ANDKW globalprotocolblock )* -> ^( GLOBALPARALLEL ( globalprotocolblock )+ ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:598:2: PARKW globalprotocolblock ( ANDKW globalprotocolblock )*
                pass 
                PARKW191 = self.match(self.input, PARKW, self.FOLLOW_PARKW_in_globalparallel2579) 
                if self._state.backtracking == 0:
                    stream_PARKW.add(PARKW191)


                self._state.following.append(self.FOLLOW_globalprotocolblock_in_globalparallel2581)
                globalprotocolblock192 = self.globalprotocolblock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_globalprotocolblock.add(globalprotocolblock192.tree)


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:598:28: ( ANDKW globalprotocolblock )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == ANDKW) :
                        alt33 = 1


                    if alt33 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:598:29: ANDKW globalprotocolblock
                        pass 
                        ANDKW193 = self.match(self.input, ANDKW, self.FOLLOW_ANDKW_in_globalparallel2584) 
                        if self._state.backtracking == 0:
                            stream_ANDKW.add(ANDKW193)


                        self._state.following.append(self.FOLLOW_globalprotocolblock_in_globalparallel2586)
                        globalprotocolblock194 = self.globalprotocolblock()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_globalprotocolblock.add(globalprotocolblock194.tree)



                    else:
                        break #loop33


                # AST Rewrite
                # elements: globalprotocolblock
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 599:2: -> ^( GLOBALPARALLEL ( globalprotocolblock )+ )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:600:2: ^( GLOBALPARALLEL ( globalprotocolblock )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(GLOBALPARALLEL, "GLOBALPARALLEL")
                    , root_1)

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:600:19: ( globalprotocolblock )+
                    if not (stream_globalprotocolblock.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_globalprotocolblock.hasNext():
                        self._adaptor.addChild(root_1, stream_globalprotocolblock.nextTree())


                    stream_globalprotocolblock.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "globalparallel"


    class globalinterruptible_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "globalinterruptible"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:607:1: globalinterruptible : ( INTERRUPTIBLEKW globalprotocolblock WITHKW '{' ( globalinterrupt )* '}' -> ^( GLOBALINTERRUPTIBLE EMPTY_SCOPE_NAME globalprotocolblock ( globalinterrupt )* ) | INTERRUPTIBLEKW scopename globalprotocolblock WITHKW '{' ( globalinterrupt )* '}' -> ^( GLOBALINTERRUPTIBLE scopename globalprotocolblock ( globalinterrupt )* ) );
    def globalinterruptible(self, ):
        retval = self.globalinterruptible_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INTERRUPTIBLEKW195 = None
        WITHKW197 = None
        char_literal198 = None
        char_literal200 = None
        INTERRUPTIBLEKW201 = None
        WITHKW204 = None
        char_literal205 = None
        char_literal207 = None
        globalprotocolblock196 = None
        globalinterrupt199 = None
        scopename202 = None
        globalprotocolblock203 = None
        globalinterrupt206 = None

        INTERRUPTIBLEKW195_tree = None
        WITHKW197_tree = None
        char_literal198_tree = None
        char_literal200_tree = None
        INTERRUPTIBLEKW201_tree = None
        WITHKW204_tree = None
        char_literal205_tree = None
        char_literal207_tree = None
        stream_WITHKW = RewriteRuleTokenStream(self._adaptor, "token WITHKW")
        stream_102 = RewriteRuleTokenStream(self._adaptor, "token 102")
        stream_103 = RewriteRuleTokenStream(self._adaptor, "token 103")
        stream_INTERRUPTIBLEKW = RewriteRuleTokenStream(self._adaptor, "token INTERRUPTIBLEKW")
        stream_globalprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule globalprotocolblock")
        stream_globalinterrupt = RewriteRuleSubtreeStream(self._adaptor, "rule globalinterrupt")
        stream_scopename = RewriteRuleSubtreeStream(self._adaptor, "rule scopename")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:607:20: ( INTERRUPTIBLEKW globalprotocolblock WITHKW '{' ( globalinterrupt )* '}' -> ^( GLOBALINTERRUPTIBLE EMPTY_SCOPE_NAME globalprotocolblock ( globalinterrupt )* ) | INTERRUPTIBLEKW scopename globalprotocolblock WITHKW '{' ( globalinterrupt )* '}' -> ^( GLOBALINTERRUPTIBLE scopename globalprotocolblock ( globalinterrupt )* ) )
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == INTERRUPTIBLEKW) :
                    LA36_1 = self.input.LA(2)

                    if (LA36_1 == 102) :
                        alt36 = 1
                    elif (LA36_1 == IDENTIFIER) :
                        alt36 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 36, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 36, 0, self.input)

                    raise nvae


                if alt36 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:608:2: INTERRUPTIBLEKW globalprotocolblock WITHKW '{' ( globalinterrupt )* '}'
                    pass 
                    INTERRUPTIBLEKW195 = self.match(self.input, INTERRUPTIBLEKW, self.FOLLOW_INTERRUPTIBLEKW_in_globalinterruptible2611) 
                    if self._state.backtracking == 0:
                        stream_INTERRUPTIBLEKW.add(INTERRUPTIBLEKW195)


                    self._state.following.append(self.FOLLOW_globalprotocolblock_in_globalinterruptible2613)
                    globalprotocolblock196 = self.globalprotocolblock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_globalprotocolblock.add(globalprotocolblock196.tree)


                    WITHKW197 = self.match(self.input, WITHKW, self.FOLLOW_WITHKW_in_globalinterruptible2615) 
                    if self._state.backtracking == 0:
                        stream_WITHKW.add(WITHKW197)


                    char_literal198 = self.match(self.input, 102, self.FOLLOW_102_in_globalinterruptible2617) 
                    if self._state.backtracking == 0:
                        stream_102.add(char_literal198)


                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:608:49: ( globalinterrupt )*
                    while True: #loop34
                        alt34 = 2
                        LA34_0 = self.input.LA(1)

                        if (LA34_0 in {IDENTIFIER, 94}) :
                            alt34 = 1


                        if alt34 == 1:
                            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:608:50: globalinterrupt
                            pass 
                            self._state.following.append(self.FOLLOW_globalinterrupt_in_globalinterruptible2620)
                            globalinterrupt199 = self.globalinterrupt()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_globalinterrupt.add(globalinterrupt199.tree)



                        else:
                            break #loop34


                    char_literal200 = self.match(self.input, 103, self.FOLLOW_103_in_globalinterruptible2624) 
                    if self._state.backtracking == 0:
                        stream_103.add(char_literal200)


                    # AST Rewrite
                    # elements: globalinterrupt, globalprotocolblock
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 609:2: -> ^( GLOBALINTERRUPTIBLE EMPTY_SCOPE_NAME globalprotocolblock ( globalinterrupt )* )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:610:2: ^( GLOBALINTERRUPTIBLE EMPTY_SCOPE_NAME globalprotocolblock ( globalinterrupt )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(GLOBALINTERRUPTIBLE, "GLOBALINTERRUPTIBLE")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(EMPTY_SCOPE_NAME, "EMPTY_SCOPE_NAME")
                        )

                        self._adaptor.addChild(root_1, stream_globalprotocolblock.nextTree())

                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:610:61: ( globalinterrupt )*
                        while stream_globalinterrupt.hasNext():
                            self._adaptor.addChild(root_1, stream_globalinterrupt.nextTree())


                        stream_globalinterrupt.reset();

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt36 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:612:2: INTERRUPTIBLEKW scopename globalprotocolblock WITHKW '{' ( globalinterrupt )* '}'
                    pass 
                    INTERRUPTIBLEKW201 = self.match(self.input, INTERRUPTIBLEKW, self.FOLLOW_INTERRUPTIBLEKW_in_globalinterruptible2646) 
                    if self._state.backtracking == 0:
                        stream_INTERRUPTIBLEKW.add(INTERRUPTIBLEKW201)


                    self._state.following.append(self.FOLLOW_scopename_in_globalinterruptible2648)
                    scopename202 = self.scopename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_scopename.add(scopename202.tree)


                    self._state.following.append(self.FOLLOW_globalprotocolblock_in_globalinterruptible2650)
                    globalprotocolblock203 = self.globalprotocolblock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_globalprotocolblock.add(globalprotocolblock203.tree)


                    WITHKW204 = self.match(self.input, WITHKW, self.FOLLOW_WITHKW_in_globalinterruptible2652) 
                    if self._state.backtracking == 0:
                        stream_WITHKW.add(WITHKW204)


                    char_literal205 = self.match(self.input, 102, self.FOLLOW_102_in_globalinterruptible2654) 
                    if self._state.backtracking == 0:
                        stream_102.add(char_literal205)


                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:612:59: ( globalinterrupt )*
                    while True: #loop35
                        alt35 = 2
                        LA35_0 = self.input.LA(1)

                        if (LA35_0 in {IDENTIFIER, 94}) :
                            alt35 = 1


                        if alt35 == 1:
                            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:612:60: globalinterrupt
                            pass 
                            self._state.following.append(self.FOLLOW_globalinterrupt_in_globalinterruptible2657)
                            globalinterrupt206 = self.globalinterrupt()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_globalinterrupt.add(globalinterrupt206.tree)



                        else:
                            break #loop35


                    char_literal207 = self.match(self.input, 103, self.FOLLOW_103_in_globalinterruptible2661) 
                    if self._state.backtracking == 0:
                        stream_103.add(char_literal207)


                    # AST Rewrite
                    # elements: globalprotocolblock, scopename, globalinterrupt
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 613:2: -> ^( GLOBALINTERRUPTIBLE scopename globalprotocolblock ( globalinterrupt )* )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:614:2: ^( GLOBALINTERRUPTIBLE scopename globalprotocolblock ( globalinterrupt )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(GLOBALINTERRUPTIBLE, "GLOBALINTERRUPTIBLE")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_scopename.nextTree())

                        self._adaptor.addChild(root_1, stream_globalprotocolblock.nextTree())

                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:614:54: ( globalinterrupt )*
                        while stream_globalinterrupt.hasNext():
                            self._adaptor.addChild(root_1, stream_globalinterrupt.nextTree())


                        stream_globalinterrupt.reset();

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "globalinterruptible"


    class globalinterrupt_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "globalinterrupt"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:617:1: globalinterrupt : message ( ',' message )* BYKW rolename ';' -> ^( GLOBALINTERRUPT rolename ( message )+ ) ;
    def globalinterrupt(self, ):
        retval = self.globalinterrupt_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal209 = None
        BYKW211 = None
        char_literal213 = None
        message208 = None
        message210 = None
        rolename212 = None

        char_literal209_tree = None
        BYKW211_tree = None
        char_literal213_tree = None
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_BYKW = RewriteRuleTokenStream(self._adaptor, "token BYKW")
        stream_96 = RewriteRuleTokenStream(self._adaptor, "token 96")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        stream_message = RewriteRuleSubtreeStream(self._adaptor, "rule message")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:617:16: ( message ( ',' message )* BYKW rolename ';' -> ^( GLOBALINTERRUPT rolename ( message )+ ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:618:2: message ( ',' message )* BYKW rolename ';'
                pass 
                self._state.following.append(self.FOLLOW_message_in_globalinterrupt2687)
                message208 = self.message()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_message.add(message208.tree)


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:618:10: ( ',' message )*
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == 96) :
                        alt37 = 1


                    if alt37 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:618:11: ',' message
                        pass 
                        char_literal209 = self.match(self.input, 96, self.FOLLOW_96_in_globalinterrupt2690) 
                        if self._state.backtracking == 0:
                            stream_96.add(char_literal209)


                        self._state.following.append(self.FOLLOW_message_in_globalinterrupt2692)
                        message210 = self.message()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_message.add(message210.tree)



                    else:
                        break #loop37


                BYKW211 = self.match(self.input, BYKW, self.FOLLOW_BYKW_in_globalinterrupt2696) 
                if self._state.backtracking == 0:
                    stream_BYKW.add(BYKW211)


                self._state.following.append(self.FOLLOW_rolename_in_globalinterrupt2698)
                rolename212 = self.rolename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rolename.add(rolename212.tree)


                char_literal213 = self.match(self.input, 99, self.FOLLOW_99_in_globalinterrupt2700) 
                if self._state.backtracking == 0:
                    stream_99.add(char_literal213)


                # AST Rewrite
                # elements: rolename, message
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 619:2: -> ^( GLOBALINTERRUPT rolename ( message )+ )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:620:2: ^( GLOBALINTERRUPT rolename ( message )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(GLOBALINTERRUPT, "GLOBALINTERRUPT")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_rolename.nextTree())

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:620:29: ( message )+
                    if not (stream_message.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_message.hasNext():
                        self._adaptor.addChild(root_1, stream_message.nextTree())


                    stream_message.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "globalinterrupt"


    class globaldo_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "globaldo"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:627:1: globaldo : ( DOKW membername roleinstantiationlist ';' -> ^( GLOBALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | DOKW membername argumentlist roleinstantiationlist ';' -> ^( GLOBALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername ) | DOKW scopename ':' membername roleinstantiationlist ';' -> ^( GLOBALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | DOKW scopename ':' membername argumentlist roleinstantiationlist ';' -> ^( GLOBALDO scopename argumentlist roleinstantiationlist membername ) );
    def globaldo(self, ):
        retval = self.globaldo_return()
        retval.start = self.input.LT(1)


        root_0 = None

        DOKW214 = None
        char_literal217 = None
        DOKW218 = None
        char_literal222 = None
        DOKW223 = None
        char_literal225 = None
        char_literal228 = None
        DOKW229 = None
        char_literal231 = None
        char_literal235 = None
        membername215 = None
        roleinstantiationlist216 = None
        membername219 = None
        argumentlist220 = None
        roleinstantiationlist221 = None
        scopename224 = None
        membername226 = None
        roleinstantiationlist227 = None
        scopename230 = None
        membername232 = None
        argumentlist233 = None
        roleinstantiationlist234 = None

        DOKW214_tree = None
        char_literal217_tree = None
        DOKW218_tree = None
        char_literal222_tree = None
        DOKW223_tree = None
        char_literal225_tree = None
        char_literal228_tree = None
        DOKW229_tree = None
        char_literal231_tree = None
        char_literal235_tree = None
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_DOKW = RewriteRuleTokenStream(self._adaptor, "token DOKW")
        stream_98 = RewriteRuleTokenStream(self._adaptor, "token 98")
        stream_argumentlist = RewriteRuleSubtreeStream(self._adaptor, "rule argumentlist")
        stream_scopename = RewriteRuleSubtreeStream(self._adaptor, "rule scopename")
        stream_roleinstantiationlist = RewriteRuleSubtreeStream(self._adaptor, "rule roleinstantiationlist")
        stream_membername = RewriteRuleSubtreeStream(self._adaptor, "rule membername")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:627:9: ( DOKW membername roleinstantiationlist ';' -> ^( GLOBALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | DOKW membername argumentlist roleinstantiationlist ';' -> ^( GLOBALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername ) | DOKW scopename ':' membername roleinstantiationlist ';' -> ^( GLOBALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | DOKW scopename ':' membername argumentlist roleinstantiationlist ';' -> ^( GLOBALDO scopename argumentlist roleinstantiationlist membername ) )
                alt38 = 4
                alt38 = self.dfa38.predict(self.input)
                if alt38 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:628:2: DOKW membername roleinstantiationlist ';'
                    pass 
                    DOKW214 = self.match(self.input, DOKW, self.FOLLOW_DOKW_in_globaldo2727) 
                    if self._state.backtracking == 0:
                        stream_DOKW.add(DOKW214)


                    self._state.following.append(self.FOLLOW_membername_in_globaldo2729)
                    membername215 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername215.tree)


                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_globaldo2731)
                    roleinstantiationlist216 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist216.tree)


                    char_literal217 = self.match(self.input, 99, self.FOLLOW_99_in_globaldo2733) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal217)


                    # AST Rewrite
                    # elements: roleinstantiationlist, membername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 629:2: -> ^( GLOBALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:630:2: ^( GLOBALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(GLOBALDO, "GLOBALDO")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(EMPTY_SCOPE_NAME, "EMPTY_SCOPE_NAME")
                        )

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(EMPTY_ARGUMENT_LIST, "EMPTY_ARGUMENT_LIST")
                        )

                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())

                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt38 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:633:2: DOKW membername argumentlist roleinstantiationlist ';'
                    pass 
                    DOKW218 = self.match(self.input, DOKW, self.FOLLOW_DOKW_in_globaldo2756) 
                    if self._state.backtracking == 0:
                        stream_DOKW.add(DOKW218)


                    self._state.following.append(self.FOLLOW_membername_in_globaldo2758)
                    membername219 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername219.tree)


                    self._state.following.append(self.FOLLOW_argumentlist_in_globaldo2760)
                    argumentlist220 = self.argumentlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_argumentlist.add(argumentlist220.tree)


                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_globaldo2762)
                    roleinstantiationlist221 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist221.tree)


                    char_literal222 = self.match(self.input, 99, self.FOLLOW_99_in_globaldo2764) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal222)


                    # AST Rewrite
                    # elements: argumentlist, roleinstantiationlist, membername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 634:2: -> ^( GLOBALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:635:2: ^( GLOBALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(GLOBALDO, "GLOBALDO")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(EMPTY_SCOPE_NAME, "EMPTY_SCOPE_NAME")
                        )

                        self._adaptor.addChild(root_1, stream_argumentlist.nextTree())

                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())

                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt38 == 3:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:637:2: DOKW scopename ':' membername roleinstantiationlist ';'
                    pass 
                    DOKW223 = self.match(self.input, DOKW, self.FOLLOW_DOKW_in_globaldo2785) 
                    if self._state.backtracking == 0:
                        stream_DOKW.add(DOKW223)


                    self._state.following.append(self.FOLLOW_scopename_in_globaldo2787)
                    scopename224 = self.scopename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_scopename.add(scopename224.tree)


                    char_literal225 = self.match(self.input, 98, self.FOLLOW_98_in_globaldo2789) 
                    if self._state.backtracking == 0:
                        stream_98.add(char_literal225)


                    self._state.following.append(self.FOLLOW_membername_in_globaldo2791)
                    membername226 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername226.tree)


                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_globaldo2793)
                    roleinstantiationlist227 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist227.tree)


                    char_literal228 = self.match(self.input, 99, self.FOLLOW_99_in_globaldo2795) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal228)


                    # AST Rewrite
                    # elements: scopename, membername, roleinstantiationlist
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 638:2: -> ^( GLOBALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:639:2: ^( GLOBALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(GLOBALDO, "GLOBALDO")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_scopename.nextTree())

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(EMPTY_ARGUMENT_LIST, "EMPTY_ARGUMENT_LIST")
                        )

                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())

                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt38 == 4:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:641:2: DOKW scopename ':' membername argumentlist roleinstantiationlist ';'
                    pass 
                    DOKW229 = self.match(self.input, DOKW, self.FOLLOW_DOKW_in_globaldo2816) 
                    if self._state.backtracking == 0:
                        stream_DOKW.add(DOKW229)


                    self._state.following.append(self.FOLLOW_scopename_in_globaldo2818)
                    scopename230 = self.scopename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_scopename.add(scopename230.tree)


                    char_literal231 = self.match(self.input, 98, self.FOLLOW_98_in_globaldo2820) 
                    if self._state.backtracking == 0:
                        stream_98.add(char_literal231)


                    self._state.following.append(self.FOLLOW_membername_in_globaldo2822)
                    membername232 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername232.tree)


                    self._state.following.append(self.FOLLOW_argumentlist_in_globaldo2824)
                    argumentlist233 = self.argumentlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_argumentlist.add(argumentlist233.tree)


                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_globaldo2826)
                    roleinstantiationlist234 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist234.tree)


                    char_literal235 = self.match(self.input, 99, self.FOLLOW_99_in_globaldo2828) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal235)


                    # AST Rewrite
                    # elements: membername, scopename, roleinstantiationlist, argumentlist
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 642:2: -> ^( GLOBALDO scopename argumentlist roleinstantiationlist membername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:643:2: ^( GLOBALDO scopename argumentlist roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(GLOBALDO, "GLOBALDO")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_scopename.nextTree())

                        self._adaptor.addChild(root_1, stream_argumentlist.nextTree())

                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())

                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "globaldo"


    class localprotocoldecl_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "localprotocoldecl"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:664:1: localprotocoldecl : ( localprotocolheader localprotocoldefinition -> ^( LOCALPROTOCOLDECL localprotocolheader localprotocoldefinition ) | localprotocolheader localprotocolinstance -> ^( LOCALPROTOCOLDECL localprotocolheader localprotocolinstance ) );
    def localprotocoldecl(self, ):
        retval = self.localprotocoldecl_return()
        retval.start = self.input.LT(1)


        root_0 = None

        localprotocolheader236 = None
        localprotocoldefinition237 = None
        localprotocolheader238 = None
        localprotocolinstance239 = None

        stream_localprotocoldefinition = RewriteRuleSubtreeStream(self._adaptor, "rule localprotocoldefinition")
        stream_localprotocolinstance = RewriteRuleSubtreeStream(self._adaptor, "rule localprotocolinstance")
        stream_localprotocolheader = RewriteRuleSubtreeStream(self._adaptor, "rule localprotocolheader")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:664:18: ( localprotocolheader localprotocoldefinition -> ^( LOCALPROTOCOLDECL localprotocolheader localprotocoldefinition ) | localprotocolheader localprotocolinstance -> ^( LOCALPROTOCOLDECL localprotocolheader localprotocolinstance ) )
                alt39 = 2
                alt39 = self.dfa39.predict(self.input)
                if alt39 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:665:2: localprotocolheader localprotocoldefinition
                    pass 
                    self._state.following.append(self.FOLLOW_localprotocolheader_in_localprotocoldecl2862)
                    localprotocolheader236 = self.localprotocolheader()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_localprotocolheader.add(localprotocolheader236.tree)


                    self._state.following.append(self.FOLLOW_localprotocoldefinition_in_localprotocoldecl2864)
                    localprotocoldefinition237 = self.localprotocoldefinition()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_localprotocoldefinition.add(localprotocoldefinition237.tree)


                    # AST Rewrite
                    # elements: localprotocolheader, localprotocoldefinition
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 666:2: -> ^( LOCALPROTOCOLDECL localprotocolheader localprotocoldefinition )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:667:2: ^( LOCALPROTOCOLDECL localprotocolheader localprotocoldefinition )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(LOCALPROTOCOLDECL, "LOCALPROTOCOLDECL")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_localprotocolheader.nextTree())

                        self._adaptor.addChild(root_1, stream_localprotocoldefinition.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt39 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:669:2: localprotocolheader localprotocolinstance
                    pass 
                    self._state.following.append(self.FOLLOW_localprotocolheader_in_localprotocoldecl2881)
                    localprotocolheader238 = self.localprotocolheader()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_localprotocolheader.add(localprotocolheader238.tree)


                    self._state.following.append(self.FOLLOW_localprotocolinstance_in_localprotocoldecl2883)
                    localprotocolinstance239 = self.localprotocolinstance()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_localprotocolinstance.add(localprotocolinstance239.tree)


                    # AST Rewrite
                    # elements: localprotocolheader, localprotocolinstance
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 670:2: -> ^( LOCALPROTOCOLDECL localprotocolheader localprotocolinstance )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:671:2: ^( LOCALPROTOCOLDECL localprotocolheader localprotocolinstance )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(LOCALPROTOCOLDECL, "LOCALPROTOCOLDECL")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_localprotocolheader.nextTree())

                        self._adaptor.addChild(root_1, stream_localprotocolinstance.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "localprotocoldecl"


    class localprotocolheader_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "localprotocolheader"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:674:1: localprotocolheader : ( LOCALKW PROTOCOLKW protocolname ATKW rolename roledecllist -> protocolname rolename EMPTY_PARAMETER_DECL_LIST roledecllist | LOCALKW PROTOCOLKW protocolname ATKW rolename parameterdecllist roledecllist -> protocolname rolename parameterdecllist roledecllist );
    def localprotocolheader(self, ):
        retval = self.localprotocolheader_return()
        retval.start = self.input.LT(1)


        root_0 = None

        LOCALKW240 = None
        PROTOCOLKW241 = None
        ATKW243 = None
        LOCALKW246 = None
        PROTOCOLKW247 = None
        ATKW249 = None
        protocolname242 = None
        rolename244 = None
        roledecllist245 = None
        protocolname248 = None
        rolename250 = None
        parameterdecllist251 = None
        roledecllist252 = None

        LOCALKW240_tree = None
        PROTOCOLKW241_tree = None
        ATKW243_tree = None
        LOCALKW246_tree = None
        PROTOCOLKW247_tree = None
        ATKW249_tree = None
        stream_LOCALKW = RewriteRuleTokenStream(self._adaptor, "token LOCALKW")
        stream_ATKW = RewriteRuleTokenStream(self._adaptor, "token ATKW")
        stream_PROTOCOLKW = RewriteRuleTokenStream(self._adaptor, "token PROTOCOLKW")
        stream_roledecllist = RewriteRuleSubtreeStream(self._adaptor, "rule roledecllist")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        stream_protocolname = RewriteRuleSubtreeStream(self._adaptor, "rule protocolname")
        stream_parameterdecllist = RewriteRuleSubtreeStream(self._adaptor, "rule parameterdecllist")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:674:20: ( LOCALKW PROTOCOLKW protocolname ATKW rolename roledecllist -> protocolname rolename EMPTY_PARAMETER_DECL_LIST roledecllist | LOCALKW PROTOCOLKW protocolname ATKW rolename parameterdecllist roledecllist -> protocolname rolename parameterdecllist roledecllist )
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if (LA40_0 == LOCALKW) :
                    LA40_1 = self.input.LA(2)

                    if (LA40_1 == PROTOCOLKW) :
                        LA40_2 = self.input.LA(3)

                        if (LA40_2 == IDENTIFIER) :
                            LA40_3 = self.input.LA(4)

                            if (LA40_3 == ATKW) :
                                LA40_4 = self.input.LA(5)

                                if (LA40_4 == IDENTIFIER) :
                                    LA40_5 = self.input.LA(6)

                                    if (LA40_5 == 94) :
                                        alt40 = 1
                                    elif (LA40_5 == 100) :
                                        alt40 = 2
                                    else:
                                        if self._state.backtracking > 0:
                                            raise BacktrackingFailed


                                        nvae = NoViableAltException("", 40, 5, self.input)

                                        raise nvae


                                else:
                                    if self._state.backtracking > 0:
                                        raise BacktrackingFailed


                                    nvae = NoViableAltException("", 40, 4, self.input)

                                    raise nvae


                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                nvae = NoViableAltException("", 40, 3, self.input)

                                raise nvae


                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            nvae = NoViableAltException("", 40, 2, self.input)

                            raise nvae


                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 40, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 40, 0, self.input)

                    raise nvae


                if alt40 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:675:2: LOCALKW PROTOCOLKW protocolname ATKW rolename roledecllist
                    pass 
                    LOCALKW240 = self.match(self.input, LOCALKW, self.FOLLOW_LOCALKW_in_localprotocolheader2904) 
                    if self._state.backtracking == 0:
                        stream_LOCALKW.add(LOCALKW240)


                    PROTOCOLKW241 = self.match(self.input, PROTOCOLKW, self.FOLLOW_PROTOCOLKW_in_localprotocolheader2906) 
                    if self._state.backtracking == 0:
                        stream_PROTOCOLKW.add(PROTOCOLKW241)


                    self._state.following.append(self.FOLLOW_protocolname_in_localprotocolheader2908)
                    protocolname242 = self.protocolname()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_protocolname.add(protocolname242.tree)


                    ATKW243 = self.match(self.input, ATKW, self.FOLLOW_ATKW_in_localprotocolheader2910) 
                    if self._state.backtracking == 0:
                        stream_ATKW.add(ATKW243)


                    self._state.following.append(self.FOLLOW_rolename_in_localprotocolheader2912)
                    rolename244 = self.rolename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_rolename.add(rolename244.tree)


                    self._state.following.append(self.FOLLOW_roledecllist_in_localprotocolheader2914)
                    roledecllist245 = self.roledecllist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roledecllist.add(roledecllist245.tree)


                    # AST Rewrite
                    # elements: roledecllist, protocolname, rolename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 676:2: -> protocolname rolename EMPTY_PARAMETER_DECL_LIST roledecllist
                        self._adaptor.addChild(root_0, stream_protocolname.nextTree())

                        self._adaptor.addChild(root_0, stream_rolename.nextTree())

                        self._adaptor.addChild(root_0, 
                        self._adaptor.createFromType(EMPTY_PARAMETER_DECL_LIST, "EMPTY_PARAMETER_DECL_LIST")
                        )

                        self._adaptor.addChild(root_0, stream_roledecllist.nextTree())




                        retval.tree = root_0




                elif alt40 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:679:2: LOCALKW PROTOCOLKW protocolname ATKW rolename parameterdecllist roledecllist
                    pass 
                    LOCALKW246 = self.match(self.input, LOCALKW, self.FOLLOW_LOCALKW_in_localprotocolheader2931) 
                    if self._state.backtracking == 0:
                        stream_LOCALKW.add(LOCALKW246)


                    PROTOCOLKW247 = self.match(self.input, PROTOCOLKW, self.FOLLOW_PROTOCOLKW_in_localprotocolheader2933) 
                    if self._state.backtracking == 0:
                        stream_PROTOCOLKW.add(PROTOCOLKW247)


                    self._state.following.append(self.FOLLOW_protocolname_in_localprotocolheader2935)
                    protocolname248 = self.protocolname()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_protocolname.add(protocolname248.tree)


                    ATKW249 = self.match(self.input, ATKW, self.FOLLOW_ATKW_in_localprotocolheader2937) 
                    if self._state.backtracking == 0:
                        stream_ATKW.add(ATKW249)


                    self._state.following.append(self.FOLLOW_rolename_in_localprotocolheader2939)
                    rolename250 = self.rolename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_rolename.add(rolename250.tree)


                    self._state.following.append(self.FOLLOW_parameterdecllist_in_localprotocolheader2941)
                    parameterdecllist251 = self.parameterdecllist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_parameterdecllist.add(parameterdecllist251.tree)


                    self._state.following.append(self.FOLLOW_roledecllist_in_localprotocolheader2943)
                    roledecllist252 = self.roledecllist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roledecllist.add(roledecllist252.tree)


                    # AST Rewrite
                    # elements: protocolname, parameterdecllist, rolename, roledecllist
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 680:2: -> protocolname rolename parameterdecllist roledecllist
                        self._adaptor.addChild(root_0, stream_protocolname.nextTree())

                        self._adaptor.addChild(root_0, stream_rolename.nextTree())

                        self._adaptor.addChild(root_0, stream_parameterdecllist.nextTree())

                        self._adaptor.addChild(root_0, stream_roledecllist.nextTree())




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "localprotocolheader"


    class localprotocoldefinition_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "localprotocoldefinition"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:688:1: localprotocoldefinition : localprotocolblock -> ^( LOCALPROTOCOLDEF localprotocolblock ) ;
    def localprotocoldefinition(self, ):
        retval = self.localprotocoldefinition_return()
        retval.start = self.input.LT(1)


        root_0 = None

        localprotocolblock253 = None

        stream_localprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule localprotocolblock")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:688:24: ( localprotocolblock -> ^( LOCALPROTOCOLDEF localprotocolblock ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:689:2: localprotocolblock
                pass 
                self._state.following.append(self.FOLLOW_localprotocolblock_in_localprotocoldefinition2967)
                localprotocolblock253 = self.localprotocolblock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_localprotocolblock.add(localprotocolblock253.tree)


                # AST Rewrite
                # elements: localprotocolblock
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 690:2: -> ^( LOCALPROTOCOLDEF localprotocolblock )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:691:2: ^( LOCALPROTOCOLDEF localprotocolblock )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LOCALPROTOCOLDEF, "LOCALPROTOCOLDEF")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_localprotocolblock.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "localprotocoldefinition"


    class localprotocolinstance_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "localprotocolinstance"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:698:1: localprotocolinstance : ( INSTANTIATESKW membername roledecllist ';' -> ^( LOCALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roledecllist membername ) | INSTANTIATESKW membername argumentlist roledecllist ';' -> ^( LOCALPROTOCOLINSTANCE argumentlist roledecllist membername ) );
    def localprotocolinstance(self, ):
        retval = self.localprotocolinstance_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INSTANTIATESKW254 = None
        char_literal257 = None
        INSTANTIATESKW258 = None
        char_literal262 = None
        membername255 = None
        roledecllist256 = None
        membername259 = None
        argumentlist260 = None
        roledecllist261 = None

        INSTANTIATESKW254_tree = None
        char_literal257_tree = None
        INSTANTIATESKW258_tree = None
        char_literal262_tree = None
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_INSTANTIATESKW = RewriteRuleTokenStream(self._adaptor, "token INSTANTIATESKW")
        stream_roledecllist = RewriteRuleSubtreeStream(self._adaptor, "rule roledecllist")
        stream_argumentlist = RewriteRuleSubtreeStream(self._adaptor, "rule argumentlist")
        stream_membername = RewriteRuleSubtreeStream(self._adaptor, "rule membername")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:698:22: ( INSTANTIATESKW membername roledecllist ';' -> ^( LOCALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roledecllist membername ) | INSTANTIATESKW membername argumentlist roledecllist ';' -> ^( LOCALPROTOCOLINSTANCE argumentlist roledecllist membername ) )
                alt41 = 2
                alt41 = self.dfa41.predict(self.input)
                if alt41 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:699:2: INSTANTIATESKW membername roledecllist ';'
                    pass 
                    INSTANTIATESKW254 = self.match(self.input, INSTANTIATESKW, self.FOLLOW_INSTANTIATESKW_in_localprotocolinstance2989) 
                    if self._state.backtracking == 0:
                        stream_INSTANTIATESKW.add(INSTANTIATESKW254)


                    self._state.following.append(self.FOLLOW_membername_in_localprotocolinstance2991)
                    membername255 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername255.tree)


                    self._state.following.append(self.FOLLOW_roledecllist_in_localprotocolinstance2993)
                    roledecllist256 = self.roledecllist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roledecllist.add(roledecllist256.tree)


                    char_literal257 = self.match(self.input, 99, self.FOLLOW_99_in_localprotocolinstance2995) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal257)


                    # AST Rewrite
                    # elements: roledecllist, membername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 700:2: -> ^( LOCALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roledecllist membername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:701:2: ^( LOCALPROTOCOLINSTANCE EMPTY_ARGUMENT_LIST roledecllist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(LOCALPROTOCOLINSTANCE, "LOCALPROTOCOLINSTANCE")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(EMPTY_ARGUMENT_LIST, "EMPTY_ARGUMENT_LIST")
                        )

                        self._adaptor.addChild(root_1, stream_roledecllist.nextTree())

                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt41 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:703:2: INSTANTIATESKW membername argumentlist roledecllist ';'
                    pass 
                    INSTANTIATESKW258 = self.match(self.input, INSTANTIATESKW, self.FOLLOW_INSTANTIATESKW_in_localprotocolinstance3014) 
                    if self._state.backtracking == 0:
                        stream_INSTANTIATESKW.add(INSTANTIATESKW258)


                    self._state.following.append(self.FOLLOW_membername_in_localprotocolinstance3016)
                    membername259 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername259.tree)


                    self._state.following.append(self.FOLLOW_argumentlist_in_localprotocolinstance3018)
                    argumentlist260 = self.argumentlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_argumentlist.add(argumentlist260.tree)


                    self._state.following.append(self.FOLLOW_roledecllist_in_localprotocolinstance3020)
                    roledecllist261 = self.roledecllist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roledecllist.add(roledecllist261.tree)


                    char_literal262 = self.match(self.input, 99, self.FOLLOW_99_in_localprotocolinstance3022) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal262)


                    # AST Rewrite
                    # elements: membername, argumentlist, roledecllist
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 704:2: -> ^( LOCALPROTOCOLINSTANCE argumentlist roledecllist membername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:705:2: ^( LOCALPROTOCOLINSTANCE argumentlist roledecllist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(LOCALPROTOCOLINSTANCE, "LOCALPROTOCOLINSTANCE")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_argumentlist.nextTree())

                        self._adaptor.addChild(root_1, stream_roledecllist.nextTree())

                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "localprotocolinstance"


    class localprotocolblock_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "localprotocolblock"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:712:1: localprotocolblock : '{' localinteractionsequence '}' -> ^( LOCALPROTOCOLBLOCK localinteractionsequence ) ;
    def localprotocolblock(self, ):
        retval = self.localprotocolblock_return()
        retval.start = self.input.LT(1)


        root_0 = None

        char_literal263 = None
        char_literal265 = None
        localinteractionsequence264 = None

        char_literal263_tree = None
        char_literal265_tree = None
        stream_102 = RewriteRuleTokenStream(self._adaptor, "token 102")
        stream_103 = RewriteRuleTokenStream(self._adaptor, "token 103")
        stream_localinteractionsequence = RewriteRuleSubtreeStream(self._adaptor, "rule localinteractionsequence")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:712:19: ( '{' localinteractionsequence '}' -> ^( LOCALPROTOCOLBLOCK localinteractionsequence ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:713:2: '{' localinteractionsequence '}'
                pass 
                char_literal263 = self.match(self.input, 102, self.FOLLOW_102_in_localprotocolblock3048) 
                if self._state.backtracking == 0:
                    stream_102.add(char_literal263)


                self._state.following.append(self.FOLLOW_localinteractionsequence_in_localprotocolblock3050)
                localinteractionsequence264 = self.localinteractionsequence()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_localinteractionsequence.add(localinteractionsequence264.tree)


                char_literal265 = self.match(self.input, 103, self.FOLLOW_103_in_localprotocolblock3052) 
                if self._state.backtracking == 0:
                    stream_103.add(char_literal265)


                # AST Rewrite
                # elements: localinteractionsequence
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 714:2: -> ^( LOCALPROTOCOLBLOCK localinteractionsequence )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:715:2: ^( LOCALPROTOCOLBLOCK localinteractionsequence )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LOCALPROTOCOLBLOCK, "LOCALPROTOCOLBLOCK")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_localinteractionsequence.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "localprotocolblock"


    class localinteractionsequence_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "localinteractionsequence"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:718:1: localinteractionsequence : ( localinteraction )* -> ^( LOCALINTERACTIONSEQUENCE ( localinteraction )* ) ;
    def localinteractionsequence(self, ):
        retval = self.localinteractionsequence_return()
        retval.start = self.input.LT(1)


        root_0 = None

        localinteraction266 = None

        stream_localinteraction = RewriteRuleSubtreeStream(self._adaptor, "rule localinteraction")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:718:25: ( ( localinteraction )* -> ^( LOCALINTERACTIONSEQUENCE ( localinteraction )* ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:719:2: ( localinteraction )*
                pass 
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:719:2: ( localinteraction )*
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 in {CHOICEKW, CONTINUEKW, DOKW, IDENTIFIER, INTERRUPTIBLEKW, PARKW, RECKW, 94}) :
                        alt42 = 1


                    if alt42 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:719:3: localinteraction
                        pass 
                        self._state.following.append(self.FOLLOW_localinteraction_in_localinteractionsequence3072)
                        localinteraction266 = self.localinteraction()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_localinteraction.add(localinteraction266.tree)



                    else:
                        break #loop42


                # AST Rewrite
                # elements: localinteraction
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 720:2: -> ^( LOCALINTERACTIONSEQUENCE ( localinteraction )* )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:721:2: ^( LOCALINTERACTIONSEQUENCE ( localinteraction )* )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LOCALINTERACTIONSEQUENCE, "LOCALINTERACTIONSEQUENCE")
                    , root_1)

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:721:29: ( localinteraction )*
                    while stream_localinteraction.hasNext():
                        self._adaptor.addChild(root_1, stream_localinteraction.nextTree())


                    stream_localinteraction.reset();

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "localinteractionsequence"


    class localinteraction_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "localinteraction"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:724:1: localinteraction : ( localsend | localreceive | localchoice | localparallel | localrecursion | localcontinue | localinterruptible | localdo );
    def localinteraction(self, ):
        retval = self.localinteraction_return()
        retval.start = self.input.LT(1)


        root_0 = None

        localsend267 = None
        localreceive268 = None
        localchoice269 = None
        localparallel270 = None
        localrecursion271 = None
        localcontinue272 = None
        localinterruptible273 = None
        localdo274 = None


        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:724:17: ( localsend | localreceive | localchoice | localparallel | localrecursion | localcontinue | localinterruptible | localdo )
                alt43 = 8
                alt43 = self.dfa43.predict(self.input)
                if alt43 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:725:2: localsend
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_localsend_in_localinteraction3096)
                    localsend267 = self.localsend()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localsend267.tree)



                elif alt43 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:727:2: localreceive
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_localreceive_in_localinteraction3101)
                    localreceive268 = self.localreceive()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localreceive268.tree)



                elif alt43 == 3:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:729:2: localchoice
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_localchoice_in_localinteraction3106)
                    localchoice269 = self.localchoice()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localchoice269.tree)



                elif alt43 == 4:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:731:2: localparallel
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_localparallel_in_localinteraction3111)
                    localparallel270 = self.localparallel()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localparallel270.tree)



                elif alt43 == 5:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:733:2: localrecursion
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_localrecursion_in_localinteraction3116)
                    localrecursion271 = self.localrecursion()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localrecursion271.tree)



                elif alt43 == 6:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:735:2: localcontinue
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_localcontinue_in_localinteraction3121)
                    localcontinue272 = self.localcontinue()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localcontinue272.tree)



                elif alt43 == 7:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:737:2: localinterruptible
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_localinterruptible_in_localinteraction3126)
                    localinterruptible273 = self.localinterruptible()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localinterruptible273.tree)



                elif alt43 == 8:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:739:2: localdo
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_localdo_in_localinteraction3131)
                    localdo274 = self.localdo()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, localdo274.tree)



                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "localinteraction"


    class localsend_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "localsend"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:748:1: localsend : message TOKW rolename ( ',' rolename )* ';' -> ^( LOCALSEND message ( rolename )+ ) ;
    def localsend(self, ):
        retval = self.localsend_return()
        retval.start = self.input.LT(1)


        root_0 = None

        TOKW276 = None
        char_literal278 = None
        char_literal280 = None
        message275 = None
        rolename277 = None
        rolename279 = None

        TOKW276_tree = None
        char_literal278_tree = None
        char_literal280_tree = None
        stream_TOKW = RewriteRuleTokenStream(self._adaptor, "token TOKW")
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_96 = RewriteRuleTokenStream(self._adaptor, "token 96")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        stream_message = RewriteRuleSubtreeStream(self._adaptor, "rule message")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:748:10: ( message TOKW rolename ( ',' rolename )* ';' -> ^( LOCALSEND message ( rolename )+ ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:749:2: message TOKW rolename ( ',' rolename )* ';'
                pass 
                self._state.following.append(self.FOLLOW_message_in_localsend3145)
                message275 = self.message()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_message.add(message275.tree)


                TOKW276 = self.match(self.input, TOKW, self.FOLLOW_TOKW_in_localsend3147) 
                if self._state.backtracking == 0:
                    stream_TOKW.add(TOKW276)


                self._state.following.append(self.FOLLOW_rolename_in_localsend3149)
                rolename277 = self.rolename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rolename.add(rolename277.tree)


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:749:24: ( ',' rolename )*
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == 96) :
                        alt44 = 1


                    if alt44 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:749:25: ',' rolename
                        pass 
                        char_literal278 = self.match(self.input, 96, self.FOLLOW_96_in_localsend3152) 
                        if self._state.backtracking == 0:
                            stream_96.add(char_literal278)


                        self._state.following.append(self.FOLLOW_rolename_in_localsend3154)
                        rolename279 = self.rolename()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_rolename.add(rolename279.tree)



                    else:
                        break #loop44


                char_literal280 = self.match(self.input, 99, self.FOLLOW_99_in_localsend3158) 
                if self._state.backtracking == 0:
                    stream_99.add(char_literal280)


                # AST Rewrite
                # elements: message, rolename
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 750:2: -> ^( LOCALSEND message ( rolename )+ )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:751:2: ^( LOCALSEND message ( rolename )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LOCALSEND, "LOCALSEND")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_message.nextTree())

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:751:22: ( rolename )+
                    if not (stream_rolename.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_rolename.hasNext():
                        self._adaptor.addChild(root_1, stream_rolename.nextTree())


                    stream_rolename.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "localsend"


    class localreceive_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "localreceive"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:754:1: localreceive : message FROMKW IDENTIFIER ';' -> ^( LOCALRECEIVE message IDENTIFIER ) ;
    def localreceive(self, ):
        retval = self.localreceive_return()
        retval.start = self.input.LT(1)


        root_0 = None

        FROMKW282 = None
        IDENTIFIER283 = None
        char_literal284 = None
        message281 = None

        FROMKW282_tree = None
        IDENTIFIER283_tree = None
        char_literal284_tree = None
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_IDENTIFIER = RewriteRuleTokenStream(self._adaptor, "token IDENTIFIER")
        stream_FROMKW = RewriteRuleTokenStream(self._adaptor, "token FROMKW")
        stream_message = RewriteRuleSubtreeStream(self._adaptor, "rule message")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:754:13: ( message FROMKW IDENTIFIER ';' -> ^( LOCALRECEIVE message IDENTIFIER ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:755:2: message FROMKW IDENTIFIER ';'
                pass 
                self._state.following.append(self.FOLLOW_message_in_localreceive3182)
                message281 = self.message()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_message.add(message281.tree)


                FROMKW282 = self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_localreceive3184) 
                if self._state.backtracking == 0:
                    stream_FROMKW.add(FROMKW282)


                IDENTIFIER283 = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_localreceive3186) 
                if self._state.backtracking == 0:
                    stream_IDENTIFIER.add(IDENTIFIER283)


                char_literal284 = self.match(self.input, 99, self.FOLLOW_99_in_localreceive3188) 
                if self._state.backtracking == 0:
                    stream_99.add(char_literal284)


                # AST Rewrite
                # elements: message, IDENTIFIER
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 756:2: -> ^( LOCALRECEIVE message IDENTIFIER )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:757:2: ^( LOCALRECEIVE message IDENTIFIER )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LOCALRECEIVE, "LOCALRECEIVE")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_message.nextTree())

                    self._adaptor.addChild(root_1, 
                    stream_IDENTIFIER.nextNode()
                    )

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "localreceive"


    class localchoice_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "localchoice"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:764:1: localchoice : CHOICEKW ATKW rolename localprotocolblock ( ORKW localprotocolblock )* -> ^( LOCALCHOICE rolename ( localprotocolblock )+ ) ;
    def localchoice(self, ):
        retval = self.localchoice_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CHOICEKW285 = None
        ATKW286 = None
        ORKW289 = None
        rolename287 = None
        localprotocolblock288 = None
        localprotocolblock290 = None

        CHOICEKW285_tree = None
        ATKW286_tree = None
        ORKW289_tree = None
        stream_ATKW = RewriteRuleTokenStream(self._adaptor, "token ATKW")
        stream_ORKW = RewriteRuleTokenStream(self._adaptor, "token ORKW")
        stream_CHOICEKW = RewriteRuleTokenStream(self._adaptor, "token CHOICEKW")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        stream_localprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule localprotocolblock")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:764:12: ( CHOICEKW ATKW rolename localprotocolblock ( ORKW localprotocolblock )* -> ^( LOCALCHOICE rolename ( localprotocolblock )+ ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:765:2: CHOICEKW ATKW rolename localprotocolblock ( ORKW localprotocolblock )*
                pass 
                CHOICEKW285 = self.match(self.input, CHOICEKW, self.FOLLOW_CHOICEKW_in_localchoice3212) 
                if self._state.backtracking == 0:
                    stream_CHOICEKW.add(CHOICEKW285)


                ATKW286 = self.match(self.input, ATKW, self.FOLLOW_ATKW_in_localchoice3214) 
                if self._state.backtracking == 0:
                    stream_ATKW.add(ATKW286)


                self._state.following.append(self.FOLLOW_rolename_in_localchoice3216)
                rolename287 = self.rolename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rolename.add(rolename287.tree)


                self._state.following.append(self.FOLLOW_localprotocolblock_in_localchoice3218)
                localprotocolblock288 = self.localprotocolblock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_localprotocolblock.add(localprotocolblock288.tree)


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:765:44: ( ORKW localprotocolblock )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == ORKW) :
                        alt45 = 1


                    if alt45 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:765:45: ORKW localprotocolblock
                        pass 
                        ORKW289 = self.match(self.input, ORKW, self.FOLLOW_ORKW_in_localchoice3221) 
                        if self._state.backtracking == 0:
                            stream_ORKW.add(ORKW289)


                        self._state.following.append(self.FOLLOW_localprotocolblock_in_localchoice3223)
                        localprotocolblock290 = self.localprotocolblock()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_localprotocolblock.add(localprotocolblock290.tree)



                    else:
                        break #loop45


                # AST Rewrite
                # elements: rolename, localprotocolblock
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 766:2: -> ^( LOCALCHOICE rolename ( localprotocolblock )+ )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:767:2: ^( LOCALCHOICE rolename ( localprotocolblock )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LOCALCHOICE, "LOCALCHOICE")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_rolename.nextTree())

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:767:25: ( localprotocolblock )+
                    if not (stream_localprotocolblock.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_localprotocolblock.hasNext():
                        self._adaptor.addChild(root_1, stream_localprotocolblock.nextTree())


                    stream_localprotocolblock.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "localchoice"


    class localrecursion_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "localrecursion"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:774:1: localrecursion : RECKW recursionlabelname localprotocolblock -> ^( LOCALRECURSION recursionlabelname localprotocolblock ) ;
    def localrecursion(self, ):
        retval = self.localrecursion_return()
        retval.start = self.input.LT(1)


        root_0 = None

        RECKW291 = None
        recursionlabelname292 = None
        localprotocolblock293 = None

        RECKW291_tree = None
        stream_RECKW = RewriteRuleTokenStream(self._adaptor, "token RECKW")
        stream_localprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule localprotocolblock")
        stream_recursionlabelname = RewriteRuleSubtreeStream(self._adaptor, "rule recursionlabelname")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:774:15: ( RECKW recursionlabelname localprotocolblock -> ^( LOCALRECURSION recursionlabelname localprotocolblock ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:775:2: RECKW recursionlabelname localprotocolblock
                pass 
                RECKW291 = self.match(self.input, RECKW, self.FOLLOW_RECKW_in_localrecursion3250) 
                if self._state.backtracking == 0:
                    stream_RECKW.add(RECKW291)


                self._state.following.append(self.FOLLOW_recursionlabelname_in_localrecursion3252)
                recursionlabelname292 = self.recursionlabelname()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_recursionlabelname.add(recursionlabelname292.tree)


                self._state.following.append(self.FOLLOW_localprotocolblock_in_localrecursion3254)
                localprotocolblock293 = self.localprotocolblock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_localprotocolblock.add(localprotocolblock293.tree)


                # AST Rewrite
                # elements: localprotocolblock, recursionlabelname
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 776:2: -> ^( LOCALRECURSION recursionlabelname localprotocolblock )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:777:2: ^( LOCALRECURSION recursionlabelname localprotocolblock )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LOCALRECURSION, "LOCALRECURSION")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_recursionlabelname.nextTree())

                    self._adaptor.addChild(root_1, stream_localprotocolblock.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "localrecursion"


    class localcontinue_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "localcontinue"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:780:1: localcontinue : CONTINUEKW recursionlabelname ';' -> ^( LOCALCONTINUE recursionlabelname ) ;
    def localcontinue(self, ):
        retval = self.localcontinue_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CONTINUEKW294 = None
        char_literal296 = None
        recursionlabelname295 = None

        CONTINUEKW294_tree = None
        char_literal296_tree = None
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_CONTINUEKW = RewriteRuleTokenStream(self._adaptor, "token CONTINUEKW")
        stream_recursionlabelname = RewriteRuleSubtreeStream(self._adaptor, "rule recursionlabelname")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:780:14: ( CONTINUEKW recursionlabelname ';' -> ^( LOCALCONTINUE recursionlabelname ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:781:2: CONTINUEKW recursionlabelname ';'
                pass 
                CONTINUEKW294 = self.match(self.input, CONTINUEKW, self.FOLLOW_CONTINUEKW_in_localcontinue3275) 
                if self._state.backtracking == 0:
                    stream_CONTINUEKW.add(CONTINUEKW294)


                self._state.following.append(self.FOLLOW_recursionlabelname_in_localcontinue3277)
                recursionlabelname295 = self.recursionlabelname()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_recursionlabelname.add(recursionlabelname295.tree)


                char_literal296 = self.match(self.input, 99, self.FOLLOW_99_in_localcontinue3279) 
                if self._state.backtracking == 0:
                    stream_99.add(char_literal296)


                # AST Rewrite
                # elements: recursionlabelname
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 782:2: -> ^( LOCALCONTINUE recursionlabelname )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:783:2: ^( LOCALCONTINUE recursionlabelname )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LOCALCONTINUE, "LOCALCONTINUE")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_recursionlabelname.nextTree())

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "localcontinue"


    class localparallel_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "localparallel"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:790:1: localparallel : PARKW localprotocolblock ( ANDKW localprotocolblock )* -> ^( LOCALPARALLEL ( localprotocolblock )+ ) ;
    def localparallel(self, ):
        retval = self.localparallel_return()
        retval.start = self.input.LT(1)


        root_0 = None

        PARKW297 = None
        ANDKW299 = None
        localprotocolblock298 = None
        localprotocolblock300 = None

        PARKW297_tree = None
        ANDKW299_tree = None
        stream_PARKW = RewriteRuleTokenStream(self._adaptor, "token PARKW")
        stream_ANDKW = RewriteRuleTokenStream(self._adaptor, "token ANDKW")
        stream_localprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule localprotocolblock")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:790:14: ( PARKW localprotocolblock ( ANDKW localprotocolblock )* -> ^( LOCALPARALLEL ( localprotocolblock )+ ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:791:2: PARKW localprotocolblock ( ANDKW localprotocolblock )*
                pass 
                PARKW297 = self.match(self.input, PARKW, self.FOLLOW_PARKW_in_localparallel3301) 
                if self._state.backtracking == 0:
                    stream_PARKW.add(PARKW297)


                self._state.following.append(self.FOLLOW_localprotocolblock_in_localparallel3303)
                localprotocolblock298 = self.localprotocolblock()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_localprotocolblock.add(localprotocolblock298.tree)


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:791:27: ( ANDKW localprotocolblock )*
                while True: #loop46
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if (LA46_0 == ANDKW) :
                        alt46 = 1


                    if alt46 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:791:28: ANDKW localprotocolblock
                        pass 
                        ANDKW299 = self.match(self.input, ANDKW, self.FOLLOW_ANDKW_in_localparallel3306) 
                        if self._state.backtracking == 0:
                            stream_ANDKW.add(ANDKW299)


                        self._state.following.append(self.FOLLOW_localprotocolblock_in_localparallel3308)
                        localprotocolblock300 = self.localprotocolblock()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_localprotocolblock.add(localprotocolblock300.tree)



                    else:
                        break #loop46


                # AST Rewrite
                # elements: localprotocolblock
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 792:2: -> ^( LOCALPARALLEL ( localprotocolblock )+ )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:793:2: ^( LOCALPARALLEL ( localprotocolblock )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LOCALPARALLEL, "LOCALPARALLEL")
                    , root_1)

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:793:18: ( localprotocolblock )+
                    if not (stream_localprotocolblock.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_localprotocolblock.hasNext():
                        self._adaptor.addChild(root_1, stream_localprotocolblock.nextTree())


                    stream_localprotocolblock.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "localparallel"


    class localinterruptible_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "localinterruptible"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:800:1: localinterruptible : ( INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' ( localcatch )* '}' -> ^( LOCALINTERRUPTIBLE scopename localprotocolblock EMPTY_LOCAL_THROW ( localcatch )* ) | INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' localthrow ( localcatch )* '}' -> ^( LOCALINTERRUPTIBLE scopename localprotocolblock localthrow ( localcatch )* ) );
    def localinterruptible(self, ):
        retval = self.localinterruptible_return()
        retval.start = self.input.LT(1)


        root_0 = None

        INTERRUPTIBLEKW301 = None
        WITHKW304 = None
        char_literal305 = None
        char_literal307 = None
        INTERRUPTIBLEKW308 = None
        WITHKW311 = None
        char_literal312 = None
        char_literal315 = None
        scopename302 = None
        localprotocolblock303 = None
        localcatch306 = None
        scopename309 = None
        localprotocolblock310 = None
        localthrow313 = None
        localcatch314 = None

        INTERRUPTIBLEKW301_tree = None
        WITHKW304_tree = None
        char_literal305_tree = None
        char_literal307_tree = None
        INTERRUPTIBLEKW308_tree = None
        WITHKW311_tree = None
        char_literal312_tree = None
        char_literal315_tree = None
        stream_WITHKW = RewriteRuleTokenStream(self._adaptor, "token WITHKW")
        stream_102 = RewriteRuleTokenStream(self._adaptor, "token 102")
        stream_103 = RewriteRuleTokenStream(self._adaptor, "token 103")
        stream_INTERRUPTIBLEKW = RewriteRuleTokenStream(self._adaptor, "token INTERRUPTIBLEKW")
        stream_localcatch = RewriteRuleSubtreeStream(self._adaptor, "rule localcatch")
        stream_scopename = RewriteRuleSubtreeStream(self._adaptor, "rule scopename")
        stream_localprotocolblock = RewriteRuleSubtreeStream(self._adaptor, "rule localprotocolblock")
        stream_localthrow = RewriteRuleSubtreeStream(self._adaptor, "rule localthrow")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:800:19: ( INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' ( localcatch )* '}' -> ^( LOCALINTERRUPTIBLE scopename localprotocolblock EMPTY_LOCAL_THROW ( localcatch )* ) | INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' localthrow ( localcatch )* '}' -> ^( LOCALINTERRUPTIBLE scopename localprotocolblock localthrow ( localcatch )* ) )
                alt49 = 2
                LA49_0 = self.input.LA(1)

                if (LA49_0 == INTERRUPTIBLEKW) :
                    LA49_1 = self.input.LA(2)

                    if (self.synpred71_Scribble()) :
                        alt49 = 1
                    elif (True) :
                        alt49 = 2
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        nvae = NoViableAltException("", 49, 1, self.input)

                        raise nvae


                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 49, 0, self.input)

                    raise nvae


                if alt49 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:805:2: INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' ( localcatch )* '}'
                    pass 
                    INTERRUPTIBLEKW301 = self.match(self.input, INTERRUPTIBLEKW, self.FOLLOW_INTERRUPTIBLEKW_in_localinterruptible3336) 
                    if self._state.backtracking == 0:
                        stream_INTERRUPTIBLEKW.add(INTERRUPTIBLEKW301)


                    self._state.following.append(self.FOLLOW_scopename_in_localinterruptible3338)
                    scopename302 = self.scopename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_scopename.add(scopename302.tree)


                    self._state.following.append(self.FOLLOW_localprotocolblock_in_localinterruptible3340)
                    localprotocolblock303 = self.localprotocolblock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_localprotocolblock.add(localprotocolblock303.tree)


                    WITHKW304 = self.match(self.input, WITHKW, self.FOLLOW_WITHKW_in_localinterruptible3342) 
                    if self._state.backtracking == 0:
                        stream_WITHKW.add(WITHKW304)


                    char_literal305 = self.match(self.input, 102, self.FOLLOW_102_in_localinterruptible3344) 
                    if self._state.backtracking == 0:
                        stream_102.add(char_literal305)


                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:805:58: ( localcatch )*
                    while True: #loop47
                        alt47 = 2
                        LA47_0 = self.input.LA(1)

                        if (LA47_0 == CATCHESKW) :
                            alt47 = 1


                        if alt47 == 1:
                            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:805:59: localcatch
                            pass 
                            self._state.following.append(self.FOLLOW_localcatch_in_localinterruptible3347)
                            localcatch306 = self.localcatch()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_localcatch.add(localcatch306.tree)



                        else:
                            break #loop47


                    char_literal307 = self.match(self.input, 103, self.FOLLOW_103_in_localinterruptible3351) 
                    if self._state.backtracking == 0:
                        stream_103.add(char_literal307)


                    # AST Rewrite
                    # elements: localprotocolblock, localcatch, scopename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 806:2: -> ^( LOCALINTERRUPTIBLE scopename localprotocolblock EMPTY_LOCAL_THROW ( localcatch )* )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:807:2: ^( LOCALINTERRUPTIBLE scopename localprotocolblock EMPTY_LOCAL_THROW ( localcatch )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(LOCALINTERRUPTIBLE, "LOCALINTERRUPTIBLE")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_scopename.nextTree())

                        self._adaptor.addChild(root_1, stream_localprotocolblock.nextTree())

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(EMPTY_LOCAL_THROW, "EMPTY_LOCAL_THROW")
                        )

                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:807:70: ( localcatch )*
                        while stream_localcatch.hasNext():
                            self._adaptor.addChild(root_1, stream_localcatch.nextTree())


                        stream_localcatch.reset();

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt49 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:809:2: INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' localthrow ( localcatch )* '}'
                    pass 
                    INTERRUPTIBLEKW308 = self.match(self.input, INTERRUPTIBLEKW, self.FOLLOW_INTERRUPTIBLEKW_in_localinterruptible3375) 
                    if self._state.backtracking == 0:
                        stream_INTERRUPTIBLEKW.add(INTERRUPTIBLEKW308)


                    self._state.following.append(self.FOLLOW_scopename_in_localinterruptible3377)
                    scopename309 = self.scopename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_scopename.add(scopename309.tree)


                    self._state.following.append(self.FOLLOW_localprotocolblock_in_localinterruptible3379)
                    localprotocolblock310 = self.localprotocolblock()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_localprotocolblock.add(localprotocolblock310.tree)


                    WITHKW311 = self.match(self.input, WITHKW, self.FOLLOW_WITHKW_in_localinterruptible3381) 
                    if self._state.backtracking == 0:
                        stream_WITHKW.add(WITHKW311)


                    char_literal312 = self.match(self.input, 102, self.FOLLOW_102_in_localinterruptible3383) 
                    if self._state.backtracking == 0:
                        stream_102.add(char_literal312)


                    self._state.following.append(self.FOLLOW_localthrow_in_localinterruptible3385)
                    localthrow313 = self.localthrow()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_localthrow.add(localthrow313.tree)


                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:809:69: ( localcatch )*
                    while True: #loop48
                        alt48 = 2
                        LA48_0 = self.input.LA(1)

                        if (LA48_0 == CATCHESKW) :
                            alt48 = 1


                        if alt48 == 1:
                            # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:809:70: localcatch
                            pass 
                            self._state.following.append(self.FOLLOW_localcatch_in_localinterruptible3388)
                            localcatch314 = self.localcatch()

                            self._state.following.pop()
                            if self._state.backtracking == 0:
                                stream_localcatch.add(localcatch314.tree)



                        else:
                            break #loop48


                    char_literal315 = self.match(self.input, 103, self.FOLLOW_103_in_localinterruptible3392) 
                    if self._state.backtracking == 0:
                        stream_103.add(char_literal315)


                    # AST Rewrite
                    # elements: scopename, localprotocolblock, localcatch, localthrow
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 810:2: -> ^( LOCALINTERRUPTIBLE scopename localprotocolblock localthrow ( localcatch )* )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:811:2: ^( LOCALINTERRUPTIBLE scopename localprotocolblock localthrow ( localcatch )* )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(LOCALINTERRUPTIBLE, "LOCALINTERRUPTIBLE")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_scopename.nextTree())

                        self._adaptor.addChild(root_1, stream_localprotocolblock.nextTree())

                        self._adaptor.addChild(root_1, stream_localthrow.nextTree())

                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:811:63: ( localcatch )*
                        while stream_localcatch.hasNext():
                            self._adaptor.addChild(root_1, stream_localcatch.nextTree())


                        stream_localcatch.reset();

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "localinterruptible"


    class localthrow_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "localthrow"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:820:1: localthrow : THROWSKW message ( ',' message )* TOKW rolename ( ',' rolename )* ';' -> ^( LOCALTHROW ( rolename )+ TOKW ( message )+ ) ;
    def localthrow(self, ):
        retval = self.localthrow_return()
        retval.start = self.input.LT(1)


        root_0 = None

        THROWSKW316 = None
        char_literal318 = None
        TOKW320 = None
        char_literal322 = None
        char_literal324 = None
        message317 = None
        message319 = None
        rolename321 = None
        rolename323 = None

        THROWSKW316_tree = None
        char_literal318_tree = None
        TOKW320_tree = None
        char_literal322_tree = None
        char_literal324_tree = None
        stream_TOKW = RewriteRuleTokenStream(self._adaptor, "token TOKW")
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_THROWSKW = RewriteRuleTokenStream(self._adaptor, "token THROWSKW")
        stream_96 = RewriteRuleTokenStream(self._adaptor, "token 96")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        stream_message = RewriteRuleSubtreeStream(self._adaptor, "rule message")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:820:11: ( THROWSKW message ( ',' message )* TOKW rolename ( ',' rolename )* ';' -> ^( LOCALTHROW ( rolename )+ TOKW ( message )+ ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:821:2: THROWSKW message ( ',' message )* TOKW rolename ( ',' rolename )* ';'
                pass 
                THROWSKW316 = self.match(self.input, THROWSKW, self.FOLLOW_THROWSKW_in_localthrow3423) 
                if self._state.backtracking == 0:
                    stream_THROWSKW.add(THROWSKW316)


                self._state.following.append(self.FOLLOW_message_in_localthrow3425)
                message317 = self.message()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_message.add(message317.tree)


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:821:19: ( ',' message )*
                while True: #loop50
                    alt50 = 2
                    LA50_0 = self.input.LA(1)

                    if (LA50_0 == 96) :
                        alt50 = 1


                    if alt50 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:821:20: ',' message
                        pass 
                        char_literal318 = self.match(self.input, 96, self.FOLLOW_96_in_localthrow3428) 
                        if self._state.backtracking == 0:
                            stream_96.add(char_literal318)


                        self._state.following.append(self.FOLLOW_message_in_localthrow3430)
                        message319 = self.message()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_message.add(message319.tree)



                    else:
                        break #loop50


                TOKW320 = self.match(self.input, TOKW, self.FOLLOW_TOKW_in_localthrow3434) 
                if self._state.backtracking == 0:
                    stream_TOKW.add(TOKW320)


                self._state.following.append(self.FOLLOW_rolename_in_localthrow3436)
                rolename321 = self.rolename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rolename.add(rolename321.tree)


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:821:48: ( ',' rolename )*
                while True: #loop51
                    alt51 = 2
                    LA51_0 = self.input.LA(1)

                    if (LA51_0 == 96) :
                        alt51 = 1


                    if alt51 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:821:49: ',' rolename
                        pass 
                        char_literal322 = self.match(self.input, 96, self.FOLLOW_96_in_localthrow3439) 
                        if self._state.backtracking == 0:
                            stream_96.add(char_literal322)


                        self._state.following.append(self.FOLLOW_rolename_in_localthrow3441)
                        rolename323 = self.rolename()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_rolename.add(rolename323.tree)



                    else:
                        break #loop51


                char_literal324 = self.match(self.input, 99, self.FOLLOW_99_in_localthrow3445) 
                if self._state.backtracking == 0:
                    stream_99.add(char_literal324)


                # AST Rewrite
                # elements: TOKW, message, rolename
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 822:2: -> ^( LOCALTHROW ( rolename )+ TOKW ( message )+ )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:823:2: ^( LOCALTHROW ( rolename )+ TOKW ( message )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LOCALTHROW, "LOCALTHROW")
                    , root_1)

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:823:15: ( rolename )+
                    if not (stream_rolename.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_rolename.hasNext():
                        self._adaptor.addChild(root_1, stream_rolename.nextTree())


                    stream_rolename.reset()

                    self._adaptor.addChild(root_1, 
                    stream_TOKW.nextNode()
                    )

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:823:32: ( message )+
                    if not (stream_message.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_message.hasNext():
                        self._adaptor.addChild(root_1, stream_message.nextTree())


                    stream_message.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "localthrow"


    class localcatch_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "localcatch"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:826:1: localcatch : CATCHESKW message ( ',' message )* FROMKW rolename ';' -> ^( LOCALCATCH rolename ( message )+ ) ;
    def localcatch(self, ):
        retval = self.localcatch_return()
        retval.start = self.input.LT(1)


        root_0 = None

        CATCHESKW325 = None
        char_literal327 = None
        FROMKW329 = None
        char_literal331 = None
        message326 = None
        message328 = None
        rolename330 = None

        CATCHESKW325_tree = None
        char_literal327_tree = None
        FROMKW329_tree = None
        char_literal331_tree = None
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_CATCHESKW = RewriteRuleTokenStream(self._adaptor, "token CATCHESKW")
        stream_96 = RewriteRuleTokenStream(self._adaptor, "token 96")
        stream_FROMKW = RewriteRuleTokenStream(self._adaptor, "token FROMKW")
        stream_rolename = RewriteRuleSubtreeStream(self._adaptor, "rule rolename")
        stream_message = RewriteRuleSubtreeStream(self._adaptor, "rule message")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:826:11: ( CATCHESKW message ( ',' message )* FROMKW rolename ';' -> ^( LOCALCATCH rolename ( message )+ ) )
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:827:2: CATCHESKW message ( ',' message )* FROMKW rolename ';'
                pass 
                CATCHESKW325 = self.match(self.input, CATCHESKW, self.FOLLOW_CATCHESKW_in_localcatch3474) 
                if self._state.backtracking == 0:
                    stream_CATCHESKW.add(CATCHESKW325)


                self._state.following.append(self.FOLLOW_message_in_localcatch3476)
                message326 = self.message()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_message.add(message326.tree)


                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:827:20: ( ',' message )*
                while True: #loop52
                    alt52 = 2
                    LA52_0 = self.input.LA(1)

                    if (LA52_0 == 96) :
                        alt52 = 1


                    if alt52 == 1:
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:827:21: ',' message
                        pass 
                        char_literal327 = self.match(self.input, 96, self.FOLLOW_96_in_localcatch3479) 
                        if self._state.backtracking == 0:
                            stream_96.add(char_literal327)


                        self._state.following.append(self.FOLLOW_message_in_localcatch3481)
                        message328 = self.message()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_message.add(message328.tree)



                    else:
                        break #loop52


                FROMKW329 = self.match(self.input, FROMKW, self.FOLLOW_FROMKW_in_localcatch3485) 
                if self._state.backtracking == 0:
                    stream_FROMKW.add(FROMKW329)


                self._state.following.append(self.FOLLOW_rolename_in_localcatch3487)
                rolename330 = self.rolename()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    stream_rolename.add(rolename330.tree)


                char_literal331 = self.match(self.input, 99, self.FOLLOW_99_in_localcatch3489) 
                if self._state.backtracking == 0:
                    stream_99.add(char_literal331)


                # AST Rewrite
                # elements: rolename, message
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 828:2: -> ^( LOCALCATCH rolename ( message )+ )
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:829:2: ^( LOCALCATCH rolename ( message )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(
                    self._adaptor.createFromType(LOCALCATCH, "LOCALCATCH")
                    , root_1)

                    self._adaptor.addChild(root_1, stream_rolename.nextTree())

                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:829:24: ( message )+
                    if not (stream_message.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_message.hasNext():
                        self._adaptor.addChild(root_1, stream_message.nextTree())


                    stream_message.reset()

                    self._adaptor.addChild(root_0, root_1)




                    retval.tree = root_0





                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "localcatch"


    class localdo_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()

            self.tree = None





    # $ANTLR start "localdo"
    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:836:1: localdo : ( DOKW membername roleinstantiationlist ';' -> ^( LOCALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | DOKW membername argumentlist roleinstantiationlist ';' -> ^( LOCALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername ) | DOKW scopename ':' membername roleinstantiationlist ';' -> ^( LOCALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | DOKW scopename ':' membername argumentlist roleinstantiationlist ';' -> ^( LOCALDO scopename argumentlist roleinstantiationlist membername ) );
    def localdo(self, ):
        retval = self.localdo_return()
        retval.start = self.input.LT(1)


        root_0 = None

        DOKW332 = None
        char_literal335 = None
        DOKW336 = None
        char_literal340 = None
        DOKW341 = None
        char_literal343 = None
        char_literal346 = None
        DOKW347 = None
        char_literal349 = None
        char_literal353 = None
        membername333 = None
        roleinstantiationlist334 = None
        membername337 = None
        argumentlist338 = None
        roleinstantiationlist339 = None
        scopename342 = None
        membername344 = None
        roleinstantiationlist345 = None
        scopename348 = None
        membername350 = None
        argumentlist351 = None
        roleinstantiationlist352 = None

        DOKW332_tree = None
        char_literal335_tree = None
        DOKW336_tree = None
        char_literal340_tree = None
        DOKW341_tree = None
        char_literal343_tree = None
        char_literal346_tree = None
        DOKW347_tree = None
        char_literal349_tree = None
        char_literal353_tree = None
        stream_99 = RewriteRuleTokenStream(self._adaptor, "token 99")
        stream_DOKW = RewriteRuleTokenStream(self._adaptor, "token DOKW")
        stream_98 = RewriteRuleTokenStream(self._adaptor, "token 98")
        stream_argumentlist = RewriteRuleSubtreeStream(self._adaptor, "rule argumentlist")
        stream_scopename = RewriteRuleSubtreeStream(self._adaptor, "rule scopename")
        stream_roleinstantiationlist = RewriteRuleSubtreeStream(self._adaptor, "rule roleinstantiationlist")
        stream_membername = RewriteRuleSubtreeStream(self._adaptor, "rule membername")
        try:
            try:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:836:8: ( DOKW membername roleinstantiationlist ';' -> ^( LOCALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | DOKW membername argumentlist roleinstantiationlist ';' -> ^( LOCALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername ) | DOKW scopename ':' membername roleinstantiationlist ';' -> ^( LOCALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername ) | DOKW scopename ':' membername argumentlist roleinstantiationlist ';' -> ^( LOCALDO scopename argumentlist roleinstantiationlist membername ) )
                alt53 = 4
                alt53 = self.dfa53.predict(self.input)
                if alt53 == 1:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:837:2: DOKW membername roleinstantiationlist ';'
                    pass 
                    DOKW332 = self.match(self.input, DOKW, self.FOLLOW_DOKW_in_localdo3516) 
                    if self._state.backtracking == 0:
                        stream_DOKW.add(DOKW332)


                    self._state.following.append(self.FOLLOW_membername_in_localdo3518)
                    membername333 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername333.tree)


                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_localdo3520)
                    roleinstantiationlist334 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist334.tree)


                    char_literal335 = self.match(self.input, 99, self.FOLLOW_99_in_localdo3522) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal335)


                    # AST Rewrite
                    # elements: roleinstantiationlist, membername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 838:2: -> ^( LOCALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:839:2: ^( LOCALDO EMPTY_SCOPE_NAME EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(LOCALDO, "LOCALDO")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(EMPTY_SCOPE_NAME, "EMPTY_SCOPE_NAME")
                        )

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(EMPTY_ARGUMENT_LIST, "EMPTY_ARGUMENT_LIST")
                        )

                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())

                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt53 == 2:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:842:2: DOKW membername argumentlist roleinstantiationlist ';'
                    pass 
                    DOKW336 = self.match(self.input, DOKW, self.FOLLOW_DOKW_in_localdo3545) 
                    if self._state.backtracking == 0:
                        stream_DOKW.add(DOKW336)


                    self._state.following.append(self.FOLLOW_membername_in_localdo3547)
                    membername337 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername337.tree)


                    self._state.following.append(self.FOLLOW_argumentlist_in_localdo3549)
                    argumentlist338 = self.argumentlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_argumentlist.add(argumentlist338.tree)


                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_localdo3551)
                    roleinstantiationlist339 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist339.tree)


                    char_literal340 = self.match(self.input, 99, self.FOLLOW_99_in_localdo3553) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal340)


                    # AST Rewrite
                    # elements: argumentlist, roleinstantiationlist, membername
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 843:2: -> ^( LOCALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:844:2: ^( LOCALDO EMPTY_SCOPE_NAME argumentlist roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(LOCALDO, "LOCALDO")
                        , root_1)

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(EMPTY_SCOPE_NAME, "EMPTY_SCOPE_NAME")
                        )

                        self._adaptor.addChild(root_1, stream_argumentlist.nextTree())

                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())

                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt53 == 3:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:846:2: DOKW scopename ':' membername roleinstantiationlist ';'
                    pass 
                    DOKW341 = self.match(self.input, DOKW, self.FOLLOW_DOKW_in_localdo3574) 
                    if self._state.backtracking == 0:
                        stream_DOKW.add(DOKW341)


                    self._state.following.append(self.FOLLOW_scopename_in_localdo3576)
                    scopename342 = self.scopename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_scopename.add(scopename342.tree)


                    char_literal343 = self.match(self.input, 98, self.FOLLOW_98_in_localdo3578) 
                    if self._state.backtracking == 0:
                        stream_98.add(char_literal343)


                    self._state.following.append(self.FOLLOW_membername_in_localdo3580)
                    membername344 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername344.tree)


                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_localdo3582)
                    roleinstantiationlist345 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist345.tree)


                    char_literal346 = self.match(self.input, 99, self.FOLLOW_99_in_localdo3584) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal346)


                    # AST Rewrite
                    # elements: membername, roleinstantiationlist, scopename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 847:2: -> ^( LOCALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:848:2: ^( LOCALDO scopename EMPTY_ARGUMENT_LIST roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(LOCALDO, "LOCALDO")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_scopename.nextTree())

                        self._adaptor.addChild(root_1, 
                        self._adaptor.createFromType(EMPTY_ARGUMENT_LIST, "EMPTY_ARGUMENT_LIST")
                        )

                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())

                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                elif alt53 == 4:
                    # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:850:2: DOKW scopename ':' membername argumentlist roleinstantiationlist ';'
                    pass 
                    DOKW347 = self.match(self.input, DOKW, self.FOLLOW_DOKW_in_localdo3605) 
                    if self._state.backtracking == 0:
                        stream_DOKW.add(DOKW347)


                    self._state.following.append(self.FOLLOW_scopename_in_localdo3607)
                    scopename348 = self.scopename()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_scopename.add(scopename348.tree)


                    char_literal349 = self.match(self.input, 98, self.FOLLOW_98_in_localdo3609) 
                    if self._state.backtracking == 0:
                        stream_98.add(char_literal349)


                    self._state.following.append(self.FOLLOW_membername_in_localdo3611)
                    membername350 = self.membername()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_membername.add(membername350.tree)


                    self._state.following.append(self.FOLLOW_argumentlist_in_localdo3613)
                    argumentlist351 = self.argumentlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_argumentlist.add(argumentlist351.tree)


                    self._state.following.append(self.FOLLOW_roleinstantiationlist_in_localdo3615)
                    roleinstantiationlist352 = self.roleinstantiationlist()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        stream_roleinstantiationlist.add(roleinstantiationlist352.tree)


                    char_literal353 = self.match(self.input, 99, self.FOLLOW_99_in_localdo3617) 
                    if self._state.backtracking == 0:
                        stream_99.add(char_literal353)


                    # AST Rewrite
                    # elements: membername, argumentlist, roleinstantiationlist, scopename
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    if self._state.backtracking == 0:
                        retval.tree = root_0
                        if retval is not None:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                        else:
                            stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                        root_0 = self._adaptor.nil()
                        # 851:2: -> ^( LOCALDO scopename argumentlist roleinstantiationlist membername )
                        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:852:2: ^( LOCALDO scopename argumentlist roleinstantiationlist membername )
                        root_1 = self._adaptor.nil()
                        root_1 = self._adaptor.becomeRoot(
                        self._adaptor.createFromType(LOCALDO, "LOCALDO")
                        , root_1)

                        self._adaptor.addChild(root_1, stream_scopename.nextTree())

                        self._adaptor.addChild(root_1, stream_argumentlist.nextTree())

                        self._adaptor.addChild(root_1, stream_roleinstantiationlist.nextTree())

                        self._adaptor.addChild(root_1, stream_membername.nextTree())

                        self._adaptor.addChild(root_0, root_1)




                        retval.tree = root_0




                retval.stop = self.input.LT(-1)


                if self._state.backtracking == 0:
                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "localdo"

    # $ANTLR start "synpred4_Scribble"
    def synpred4_Scribble_fragment(self, ):
        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:237:2: ( payloadtypename )
        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:237:2: payloadtypename
        pass 
        root_0 = self._adaptor.nil()


        self._state.following.append(self.FOLLOW_payloadtypename_in_synpred4_Scribble1107)
        self.payloadtypename()

        self._state.following.pop()




    # $ANTLR end "synpred4_Scribble"



    # $ANTLR start "synpred17_Scribble"
    def synpred17_Scribble_fragment(self, ):
        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:352:2: ( payloadtypename )
        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:352:2: payloadtypename
        pass 
        root_0 = self._adaptor.nil()


        self._state.following.append(self.FOLLOW_payloadtypename_in_synpred17_Scribble1627)
        self.payloadtypename()

        self._state.following.pop()




    # $ANTLR end "synpred17_Scribble"



    # $ANTLR start "synpred18_Scribble"
    def synpred18_Scribble_fragment(self, ):
        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:356:2: ( parametername )
        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:356:2: parametername
        pass 
        root_0 = self._adaptor.nil()


        self._state.following.append(self.FOLLOW_parametername_in_synpred18_Scribble1644)
        self.parametername()

        self._state.following.pop()




    # $ANTLR end "synpred18_Scribble"



    # $ANTLR start "synpred19_Scribble"
    def synpred19_Scribble_fragment(self, ):
        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:361:2: ( annotationname ':' payloadtypename )
        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:361:2: annotationname ':' payloadtypename
        pass 
        root_0 = self._adaptor.nil()


        self._state.following.append(self.FOLLOW_annotationname_in_synpred19_Scribble1664)
        self.annotationname()

        self._state.following.pop()


        self.match(self.input, 98, self.FOLLOW_98_in_synpred19_Scribble1666)


        self._state.following.append(self.FOLLOW_payloadtypename_in_synpred19_Scribble1668)
        self.payloadtypename()

        self._state.following.pop()




    # $ANTLR end "synpred19_Scribble"



    # $ANTLR start "synpred35_Scribble"
    def synpred35_Scribble_fragment(self, ):
        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:500:2: ( payloadtypename )
        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:500:2: payloadtypename
        pass 
        root_0 = self._adaptor.nil()


        self._state.following.append(self.FOLLOW_payloadtypename_in_synpred35_Scribble2254)
        self.payloadtypename()

        self._state.following.pop()




    # $ANTLR end "synpred35_Scribble"



    # $ANTLR start "synpred36_Scribble"
    def synpred36_Scribble_fragment(self, ):
        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:504:2: ( payloadtypename ASKW parametername )
        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:504:2: payloadtypename ASKW parametername
        pass 
        root_0 = self._adaptor.nil()


        self._state.following.append(self.FOLLOW_payloadtypename_in_synpred36_Scribble2269)
        self.payloadtypename()

        self._state.following.pop()


        self.match(self.input, ASKW, self.FOLLOW_ASKW_in_synpred36_Scribble2271)


        self._state.following.append(self.FOLLOW_parametername_in_synpred36_Scribble2273)
        self.parametername()

        self._state.following.pop()




    # $ANTLR end "synpred36_Scribble"



    # $ANTLR start "synpred37_Scribble"
    def synpred37_Scribble_fragment(self, ):
        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:508:2: ( parametername )
        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:508:2: parametername
        pass 
        root_0 = self._adaptor.nil()


        self._state.following.append(self.FOLLOW_parametername_in_synpred37_Scribble2290)
        self.parametername()

        self._state.following.pop()




    # $ANTLR end "synpred37_Scribble"



    # $ANTLR start "synpred71_Scribble"
    def synpred71_Scribble_fragment(self, ):
        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:805:2: ( INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' ( localcatch )* '}' )
        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:805:2: INTERRUPTIBLEKW scopename localprotocolblock WITHKW '{' ( localcatch )* '}'
        pass 
        root_0 = self._adaptor.nil()


        self.match(self.input, INTERRUPTIBLEKW, self.FOLLOW_INTERRUPTIBLEKW_in_synpred71_Scribble3336)


        self._state.following.append(self.FOLLOW_scopename_in_synpred71_Scribble3338)
        self.scopename()

        self._state.following.pop()


        self._state.following.append(self.FOLLOW_localprotocolblock_in_synpred71_Scribble3340)
        self.localprotocolblock()

        self._state.following.pop()


        self.match(self.input, WITHKW, self.FOLLOW_WITHKW_in_synpred71_Scribble3342)


        self.match(self.input, 102, self.FOLLOW_102_in_synpred71_Scribble3344)


        # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:805:58: ( localcatch )*
        while True: #loop56
            alt56 = 2
            LA56_0 = self.input.LA(1)

            if (LA56_0 == CATCHESKW) :
                alt56 = 1


            if alt56 == 1:
                # C:\\Tools\\myPythonScrib\\scribble-python\\Scribble.g:805:59: localcatch
                pass 
                self._state.following.append(self.FOLLOW_localcatch_in_synpred71_Scribble3347)
                self.localcatch()

                self._state.following.pop()



            else:
                break #loop56


        self.match(self.input, 103, self.FOLLOW_103_in_synpred71_Scribble3351)




    # $ANTLR end "synpred71_Scribble"




    def synpred36_Scribble(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred36_Scribble_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred18_Scribble(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred18_Scribble_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred17_Scribble(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred17_Scribble_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred19_Scribble(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred19_Scribble_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred4_Scribble(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred4_Scribble_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred71_Scribble(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred71_Scribble_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred35_Scribble(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred35_Scribble_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred37_Scribble(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred37_Scribble_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        "\7\uffff"
        )

    DFA9_eof = DFA.unpack(
        "\7\uffff"
        )

    DFA9_min = DFA.unpack(
        "\1\51\1\50\1\7\1\50\2\uffff\1\7"
        )

    DFA9_max = DFA.unpack(
        "\1\51\1\50\1\143\1\50\2\uffff\1\143"
        )

    DFA9_accept = DFA.unpack(
        "\4\uffff\1\1\1\2\1\uffff"
        )

    DFA9_special = DFA.unpack(
        "\7\uffff"
        )


    DFA9_transition = [
        DFA.unpack("\1\1"),
        DFA.unpack("\1\2"),
        DFA.unpack("\1\5\131\uffff\1\3\1\uffff\1\4"),
        DFA.unpack("\1\6"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\5\131\uffff\1\3\1\uffff\1\4")
    ]

    # class definition for DFA #9

    class DFA9(DFA):
        pass


    # lookup tables for DFA #10

    DFA10_eot = DFA.unpack(
        "\11\uffff"
        )

    DFA10_eof = DFA.unpack(
        "\11\uffff"
        )

    DFA10_min = DFA.unpack(
        "\1\31\1\50\1\51\2\50\1\51\1\7\2\uffff"
        )

    DFA10_max = DFA.unpack(
        "\1\31\1\50\1\141\2\50\1\141\1\143\2\uffff"
        )

    DFA10_accept = DFA.unpack(
        "\7\uffff\1\1\1\2"
        )

    DFA10_special = DFA.unpack(
        "\11\uffff"
        )


    DFA10_transition = [
        DFA.unpack("\1\1"),
        DFA.unpack("\1\2"),
        DFA.unpack("\1\4\67\uffff\1\3"),
        DFA.unpack("\1\5"),
        DFA.unpack("\1\6"),
        DFA.unpack("\1\4\67\uffff\1\3"),
        DFA.unpack("\1\10\133\uffff\1\7"),
        DFA.unpack(""),
        DFA.unpack("")
    ]

    # class definition for DFA #10

    class DFA10(DFA):
        pass


    # lookup tables for DFA #17

    DFA17_eot = DFA.unpack(
        "\57\uffff"
        )

    DFA17_eof = DFA.unpack(
        "\57\uffff"
        )

    DFA17_min = DFA.unpack(
        "\1\40\1\117\1\50\1\136\1\125\1\126\3\50\3\7\1\125\1\54\1\50\1\126"
        "\1\136\3\50\2\uffff\1\137\2\50\1\125\2\140\3\7\4\50\1\7\1\137\2"
        "\140\1\125\1\54\2\50\1\137\1\7\1\50\1\137"
        )

    DFA17_max = DFA.unpack(
        "\1\40\1\117\1\50\1\144\1\125\1\132\3\50\1\140\2\145\1\125\1\146"
        "\1\50\1\132\1\136\3\50\2\uffff\1\140\2\50\1\125\2\145\1\140\2\145"
        "\4\50\2\140\2\145\1\125\1\146\2\50\2\140\1\50\1\140"
        )

    DFA17_accept = DFA.unpack(
        "\24\uffff\1\1\1\2\31\uffff"
        )

    DFA17_special = DFA.unpack(
        "\57\uffff"
        )


    DFA17_transition = [
        DFA.unpack("\1\1"),
        DFA.unpack("\1\2"),
        DFA.unpack("\1\3"),
        DFA.unpack("\1\4\5\uffff\1\5"),
        DFA.unpack("\1\6"),
        DFA.unpack("\1\10\3\uffff\1\7"),
        DFA.unpack("\1\11"),
        DFA.unpack("\1\12"),
        DFA.unpack("\1\13"),
        DFA.unpack("\1\16\127\uffff\1\15\1\14"),
        DFA.unpack("\1\21\130\uffff\1\17\4\uffff\1\20"),
        DFA.unpack("\1\22\130\uffff\1\17\4\uffff\1\20"),
        DFA.unpack("\1\23"),
        DFA.unpack("\1\25\71\uffff\1\24"),
        DFA.unpack("\1\26"),
        DFA.unpack("\1\30\3\uffff\1\27"),
        DFA.unpack("\1\31"),
        DFA.unpack("\1\32"),
        DFA.unpack("\1\33"),
        DFA.unpack("\1\34"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\15\1\14"),
        DFA.unpack("\1\35"),
        DFA.unpack("\1\36"),
        DFA.unpack("\1\37"),
        DFA.unpack("\1\17\4\uffff\1\20"),
        DFA.unpack("\1\17\4\uffff\1\20"),
        DFA.unpack("\1\40\127\uffff\1\15\1\14"),
        DFA.unpack("\1\41\130\uffff\1\17\4\uffff\1\20"),
        DFA.unpack("\1\42\130\uffff\1\17\4\uffff\1\20"),
        DFA.unpack("\1\43"),
        DFA.unpack("\1\44"),
        DFA.unpack("\1\45"),
        DFA.unpack("\1\46"),
        DFA.unpack("\1\51\127\uffff\1\50\1\47"),
        DFA.unpack("\1\15\1\14"),
        DFA.unpack("\1\17\4\uffff\1\20"),
        DFA.unpack("\1\17\4\uffff\1\20"),
        DFA.unpack("\1\52"),
        DFA.unpack("\1\25\71\uffff\1\24"),
        DFA.unpack("\1\53"),
        DFA.unpack("\1\54"),
        DFA.unpack("\1\50\1\47"),
        DFA.unpack("\1\55\127\uffff\1\50\1\47"),
        DFA.unpack("\1\56"),
        DFA.unpack("\1\50\1\47")
    ]

    # class definition for DFA #17

    class DFA17(DFA):
        pass


    # lookup tables for DFA #23

    DFA23_eot = DFA.unpack(
        "\7\uffff"
        )

    DFA23_eof = DFA.unpack(
        "\7\uffff"
        )

    DFA23_min = DFA.unpack(
        "\1\54\1\50\1\136\1\uffff\1\50\1\uffff\1\136"
        )

    DFA23_max = DFA.unpack(
        "\1\54\1\50\1\144\1\uffff\1\50\1\uffff\1\144"
        )

    DFA23_accept = DFA.unpack(
        "\3\uffff\1\1\1\uffff\1\2\1\uffff"
        )

    DFA23_special = DFA.unpack(
        "\7\uffff"
        )


    DFA23_transition = [
        DFA.unpack("\1\1"),
        DFA.unpack("\1\2"),
        DFA.unpack("\1\3\2\uffff\1\4\2\uffff\1\5"),
        DFA.unpack(""),
        DFA.unpack("\1\6"),
        DFA.unpack(""),
        DFA.unpack("\1\3\2\uffff\1\4\2\uffff\1\5")
    ]

    # class definition for DFA #23

    class DFA23(DFA):
        pass


    # lookup tables for DFA #27

    DFA27_eot = DFA.unpack(
        "\34\uffff"
        )

    DFA27_eof = DFA.unpack(
        "\3\uffff\1\11\11\uffff\1\11\16\uffff"
        )

    DFA27_min = DFA.unpack(
        "\2\50\2\7\1\137\2\50\4\uffff\2\50\1\7\1\137\1\0\2\137\2\50\2\uffff"
        "\1\50\3\137\1\50\1\137"
        )

    DFA27_max = DFA.unpack(
        "\1\136\1\137\1\136\1\145\1\142\1\137\1\50\4\uffff\2\50\1\145\1\142"
        "\1\0\1\142\1\140\2\50\2\uffff\1\50\1\142\2\140\1\50\1\140"
        )

    DFA27_accept = DFA.unpack(
        "\7\uffff\1\3\1\5\1\1\1\2\11\uffff\1\4\1\6\6\uffff"
        )

    DFA27_special = DFA.unpack(
        "\2\uffff\1\1\14\uffff\1\0\14\uffff"
        )


    DFA27_transition = [
        DFA.unpack("\1\2\65\uffff\1\1"),
        DFA.unpack("\1\4\66\uffff\1\3"),
        DFA.unpack("\1\6\126\uffff\1\5"),
        DFA.unpack("\1\12\130\uffff\1\11\4\uffff\1\11"),
        DFA.unpack("\1\3\1\13\1\uffff\1\14"),
        DFA.unpack("\1\16\66\uffff\1\15"),
        DFA.unpack("\1\17"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\20"),
        DFA.unpack("\1\21"),
        DFA.unpack("\1\12\130\uffff\1\11\4\uffff\1\11"),
        DFA.unpack("\1\15\1\22\1\uffff\1\23"),
        DFA.unpack("\1\uffff"),
        DFA.unpack("\1\3\1\13\1\uffff\1\26"),
        DFA.unpack("\1\3\1\13"),
        DFA.unpack("\1\27"),
        DFA.unpack("\1\30"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\31"),
        DFA.unpack("\1\15\1\22\1\uffff\1\32"),
        DFA.unpack("\1\15\1\22"),
        DFA.unpack("\1\3\1\13"),
        DFA.unpack("\1\33"),
        DFA.unpack("\1\15\1\22")
    ]

    # class definition for DFA #27

    class DFA27(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA27_15 = input.LA(1)

                 
                index27_15 = input.index()
                input.rewind()

                s = -1
                if (self.synpred36_Scribble()):
                    s = 20

                elif (True):
                    s = 21

                 
                input.seek(index27_15)

                if s >= 0:
                    return s
            elif s == 1: 
                LA27_2 = input.LA(1)

                 
                index27_2 = input.index()
                input.rewind()

                s = -1
                if (LA27_2 == 94):
                    s = 5

                elif (LA27_2 == ASKW):
                    s = 6

                elif (self.synpred35_Scribble()):
                    s = 7

                elif (self.synpred37_Scribble()):
                    s = 8

                 
                input.seek(index27_2)

                if s >= 0:
                    return s

            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException(self_.getDescription(), 27, _s, input)
            self_.error(nvae)
            raise nvae

    # lookup tables for DFA #38

    DFA38_eot = DFA.unpack(
        "\15\uffff"
        )

    DFA38_eof = DFA.unpack(
        "\15\uffff"
        )

    DFA38_min = DFA.unpack(
        "\1\17\1\50\1\136\1\uffff\1\50\1\uffff\1\50\2\136\1\uffff\1\50\1"
        "\uffff\1\136"
        )

    DFA38_max = DFA.unpack(
        "\1\17\1\50\1\144\1\uffff\1\50\1\uffff\1\50\2\144\1\uffff\1\50\1"
        "\uffff\1\144"
        )

    DFA38_accept = DFA.unpack(
        "\3\uffff\1\1\1\uffff\1\2\3\uffff\1\3\1\uffff\1\4\1\uffff"
        )

    DFA38_special = DFA.unpack(
        "\15\uffff"
        )


    DFA38_transition = [
        DFA.unpack("\1\1"),
        DFA.unpack("\1\2"),
        DFA.unpack("\1\3\2\uffff\1\4\1\6\1\uffff\1\5"),
        DFA.unpack(""),
        DFA.unpack("\1\7"),
        DFA.unpack(""),
        DFA.unpack("\1\10"),
        DFA.unpack("\1\3\2\uffff\1\4\2\uffff\1\5"),
        DFA.unpack("\1\11\2\uffff\1\12\2\uffff\1\13"),
        DFA.unpack(""),
        DFA.unpack("\1\14"),
        DFA.unpack(""),
        DFA.unpack("\1\11\2\uffff\1\12\2\uffff\1\13")
    ]

    # class definition for DFA #38

    class DFA38(DFA):
        pass


    # lookup tables for DFA #39

    DFA39_eot = DFA.unpack(
        "\61\uffff"
        )

    DFA39_eof = DFA.unpack(
        "\61\uffff"
        )

    DFA39_min = DFA.unpack(
        "\1\71\1\117\1\50\1\10\1\50\1\136\1\125\1\126\3\50\3\7\1\125\1\54"
        "\1\50\1\126\1\136\3\50\2\uffff\1\137\2\50\1\125\2\140\3\7\4\50\1"
        "\7\1\137\2\140\1\125\1\54\2\50\1\137\1\7\1\50\1\137"
        )

    DFA39_max = DFA.unpack(
        "\1\71\1\117\1\50\1\10\1\50\1\144\1\125\1\132\3\50\1\140\2\145\1"
        "\125\1\146\1\50\1\132\1\136\3\50\2\uffff\1\140\2\50\1\125\2\145"
        "\1\140\2\145\4\50\2\140\2\145\1\125\1\146\2\50\2\140\1\50\1\140"
        )

    DFA39_accept = DFA.unpack(
        "\26\uffff\1\1\1\2\31\uffff"
        )

    DFA39_special = DFA.unpack(
        "\61\uffff"
        )


    DFA39_transition = [
        DFA.unpack("\1\1"),
        DFA.unpack("\1\2"),
        DFA.unpack("\1\3"),
        DFA.unpack("\1\4"),
        DFA.unpack("\1\5"),
        DFA.unpack("\1\6\5\uffff\1\7"),
        DFA.unpack("\1\10"),
        DFA.unpack("\1\12\3\uffff\1\11"),
        DFA.unpack("\1\13"),
        DFA.unpack("\1\14"),
        DFA.unpack("\1\15"),
        DFA.unpack("\1\20\127\uffff\1\17\1\16"),
        DFA.unpack("\1\23\130\uffff\1\21\4\uffff\1\22"),
        DFA.unpack("\1\24\130\uffff\1\21\4\uffff\1\22"),
        DFA.unpack("\1\25"),
        DFA.unpack("\1\27\71\uffff\1\26"),
        DFA.unpack("\1\30"),
        DFA.unpack("\1\32\3\uffff\1\31"),
        DFA.unpack("\1\33"),
        DFA.unpack("\1\34"),
        DFA.unpack("\1\35"),
        DFA.unpack("\1\36"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\17\1\16"),
        DFA.unpack("\1\37"),
        DFA.unpack("\1\40"),
        DFA.unpack("\1\41"),
        DFA.unpack("\1\21\4\uffff\1\22"),
        DFA.unpack("\1\21\4\uffff\1\22"),
        DFA.unpack("\1\42\127\uffff\1\17\1\16"),
        DFA.unpack("\1\43\130\uffff\1\21\4\uffff\1\22"),
        DFA.unpack("\1\44\130\uffff\1\21\4\uffff\1\22"),
        DFA.unpack("\1\45"),
        DFA.unpack("\1\46"),
        DFA.unpack("\1\47"),
        DFA.unpack("\1\50"),
        DFA.unpack("\1\53\127\uffff\1\52\1\51"),
        DFA.unpack("\1\17\1\16"),
        DFA.unpack("\1\21\4\uffff\1\22"),
        DFA.unpack("\1\21\4\uffff\1\22"),
        DFA.unpack("\1\54"),
        DFA.unpack("\1\27\71\uffff\1\26"),
        DFA.unpack("\1\55"),
        DFA.unpack("\1\56"),
        DFA.unpack("\1\52\1\51"),
        DFA.unpack("\1\57\127\uffff\1\52\1\51"),
        DFA.unpack("\1\60"),
        DFA.unpack("\1\52\1\51")
    ]

    # class definition for DFA #39

    class DFA39(DFA):
        pass


    # lookup tables for DFA #41

    DFA41_eot = DFA.unpack(
        "\7\uffff"
        )

    DFA41_eof = DFA.unpack(
        "\7\uffff"
        )

    DFA41_min = DFA.unpack(
        "\1\54\1\50\1\136\1\uffff\1\50\1\uffff\1\136"
        )

    DFA41_max = DFA.unpack(
        "\1\54\1\50\1\144\1\uffff\1\50\1\uffff\1\144"
        )

    DFA41_accept = DFA.unpack(
        "\3\uffff\1\1\1\uffff\1\2\1\uffff"
        )

    DFA41_special = DFA.unpack(
        "\7\uffff"
        )


    DFA41_transition = [
        DFA.unpack("\1\1"),
        DFA.unpack("\1\2"),
        DFA.unpack("\1\3\2\uffff\1\4\2\uffff\1\5"),
        DFA.unpack(""),
        DFA.unpack("\1\6"),
        DFA.unpack(""),
        DFA.unpack("\1\3\2\uffff\1\4\2\uffff\1\5")
    ]

    # class definition for DFA #41

    class DFA41(DFA):
        pass


    # lookup tables for DFA #43

    DFA43_eot = DFA.unpack(
        "\34\uffff"
        )

    DFA43_eof = DFA.unpack(
        "\34\uffff"
        )

    DFA43_min = DFA.unpack(
        "\1\13\1\50\1\31\6\uffff\1\31\1\137\1\50\2\uffff\2\50\1\31\3\137"
        "\3\50\3\137\1\50\1\137"
        )

    DFA43_max = DFA.unpack(
        "\1\136\1\137\1\136\6\uffff\1\131\1\142\1\137\2\uffff\2\50\1\131"
        "\2\142\1\140\3\50\1\142\2\140\1\50\1\140"
        )

    DFA43_accept = DFA.unpack(
        "\3\uffff\1\3\1\4\1\5\1\6\1\7\1\10\3\uffff\1\1\1\2\16\uffff"
        )

    DFA43_special = DFA.unpack(
        "\34\uffff"
        )


    DFA43_transition = [
        DFA.unpack("\1\3\1\uffff\1\6\1\uffff\1\10\30\uffff\1\2\4\uffff\1"
        "\7\35\uffff\1\4\4\uffff\1\5\15\uffff\1\1"),
        DFA.unpack("\1\12\66\uffff\1\11"),
        DFA.unpack("\1\15\77\uffff\1\14\4\uffff\1\13"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\15\77\uffff\1\14"),
        DFA.unpack("\1\11\1\16\1\uffff\1\17"),
        DFA.unpack("\1\21\66\uffff\1\20"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\22"),
        DFA.unpack("\1\23"),
        DFA.unpack("\1\15\77\uffff\1\14"),
        DFA.unpack("\1\20\1\24\1\uffff\1\25"),
        DFA.unpack("\1\11\1\16\1\uffff\1\26"),
        DFA.unpack("\1\11\1\16"),
        DFA.unpack("\1\27"),
        DFA.unpack("\1\30"),
        DFA.unpack("\1\31"),
        DFA.unpack("\1\20\1\24\1\uffff\1\32"),
        DFA.unpack("\1\20\1\24"),
        DFA.unpack("\1\11\1\16"),
        DFA.unpack("\1\33"),
        DFA.unpack("\1\20\1\24")
    ]

    # class definition for DFA #43

    class DFA43(DFA):
        pass


    # lookup tables for DFA #53

    DFA53_eot = DFA.unpack(
        "\15\uffff"
        )

    DFA53_eof = DFA.unpack(
        "\15\uffff"
        )

    DFA53_min = DFA.unpack(
        "\1\17\1\50\1\136\1\uffff\1\50\1\uffff\1\50\2\136\1\uffff\1\50\1"
        "\uffff\1\136"
        )

    DFA53_max = DFA.unpack(
        "\1\17\1\50\1\144\1\uffff\1\50\1\uffff\1\50\2\144\1\uffff\1\50\1"
        "\uffff\1\144"
        )

    DFA53_accept = DFA.unpack(
        "\3\uffff\1\1\1\uffff\1\2\3\uffff\1\3\1\uffff\1\4\1\uffff"
        )

    DFA53_special = DFA.unpack(
        "\15\uffff"
        )


    DFA53_transition = [
        DFA.unpack("\1\1"),
        DFA.unpack("\1\2"),
        DFA.unpack("\1\3\2\uffff\1\4\1\6\1\uffff\1\5"),
        DFA.unpack(""),
        DFA.unpack("\1\7"),
        DFA.unpack(""),
        DFA.unpack("\1\10"),
        DFA.unpack("\1\3\2\uffff\1\4\2\uffff\1\5"),
        DFA.unpack("\1\11\2\uffff\1\12\2\uffff\1\13"),
        DFA.unpack(""),
        DFA.unpack("\1\14"),
        DFA.unpack(""),
        DFA.unpack("\1\11\2\uffff\1\12\2\uffff\1\13")
    ]

    # class definition for DFA #53

    class DFA53(DFA):
        pass


 

    FOLLOW_IDENTIFIER_in_rolename998 = frozenset([1])
    FOLLOW_IDENTIFIER_in_payloadtypename1004 = frozenset([1])
    FOLLOW_IDENTIFIER_in_protocolname1010 = frozenset([1])
    FOLLOW_IDENTIFIER_in_parametername1016 = frozenset([1])
    FOLLOW_IDENTIFIER_in_annotationname1022 = frozenset([1])
    FOLLOW_IDENTIFIER_in_recursionlabelname1028 = frozenset([1])
    FOLLOW_IDENTIFIER_in_scopename1034 = frozenset([1])
    FOLLOW_IDENTIFIER_in_modulename1050 = frozenset([97])
    FOLLOW_97_in_modulename1053 = frozenset([40])
    FOLLOW_IDENTIFIER_in_modulename1055 = frozenset([97])
    FOLLOW_97_in_modulename1059 = frozenset([40])
    FOLLOW_IDENTIFIER_in_modulename1061 = frozenset([1])
    FOLLOW_IDENTIFIER_in_modulename1075 = frozenset([1])
    FOLLOW_simplemembername_in_membername1093 = frozenset([1])
    FOLLOW_fullmembername_in_membername1098 = frozenset([1])
    FOLLOW_payloadtypename_in_simplemembername1107 = frozenset([1])
    FOLLOW_protocolname_in_simplemembername1112 = frozenset([1])
    FOLLOW_modulename_in_fullmembername1124 = frozenset([97])
    FOLLOW_97_in_fullmembername1126 = frozenset([40])
    FOLLOW_simplemembername_in_fullmembername1128 = frozenset([1])
    FOLLOW_moduledecl_in_module1151 = frozenset([1, 25, 32, 41, 57, 90])
    FOLLOW_importdecl_in_module1154 = frozenset([1, 25, 32, 41, 57, 90])
    FOLLOW_payloadtypedecl_in_module1159 = frozenset([1, 32, 57, 90])
    FOLLOW_protocoldecl_in_module1164 = frozenset([1, 32, 57])
    FOLLOW_MODULEKW_in_moduledecl1209 = frozenset([40])
    FOLLOW_modulename_in_moduledecl1211 = frozenset([99])
    FOLLOW_99_in_moduledecl1213 = frozenset([1])
    FOLLOW_importmodule_in_importdecl1235 = frozenset([1])
    FOLLOW_importmember_in_importdecl1240 = frozenset([1])
    FOLLOW_IMPORTKW_in_importmodule1249 = frozenset([40])
    FOLLOW_modulename_in_importmodule1251 = frozenset([99])
    FOLLOW_99_in_importmodule1253 = frozenset([1])
    FOLLOW_IMPORTKW_in_importmodule1271 = frozenset([40])
    FOLLOW_modulename_in_importmodule1273 = frozenset([7])
    FOLLOW_ASKW_in_importmodule1275 = frozenset([40])
    FOLLOW_IDENTIFIER_in_importmodule1277 = frozenset([99])
    FOLLOW_99_in_importmodule1279 = frozenset([1])
    FOLLOW_FROMKW_in_importmember1350 = frozenset([40])
    FOLLOW_modulename_in_importmember1352 = frozenset([41])
    FOLLOW_IMPORTKW_in_importmember1354 = frozenset([40])
    FOLLOW_simplemembername_in_importmember1356 = frozenset([99])
    FOLLOW_99_in_importmember1358 = frozenset([1])
    FOLLOW_FROMKW_in_importmember1424 = frozenset([40])
    FOLLOW_modulename_in_importmember1426 = frozenset([41])
    FOLLOW_IMPORTKW_in_importmember1428 = frozenset([40])
    FOLLOW_simplemembername_in_importmember1430 = frozenset([7])
    FOLLOW_ASKW_in_importmember1432 = frozenset([40])
    FOLLOW_IDENTIFIER_in_importmember1434 = frozenset([99])
    FOLLOW_99_in_importmember1436 = frozenset([1])
    FOLLOW_TYPEKW_in_payloadtypedecl1466 = frozenset([100])
    FOLLOW_100_in_payloadtypedecl1468 = frozenset([40])
    FOLLOW_IDENTIFIER_in_payloadtypedecl1470 = frozenset([101])
    FOLLOW_101_in_payloadtypedecl1472 = frozenset([24])
    FOLLOW_EXTIDENTIFIER_in_payloadtypedecl1474 = frozenset([25])
    FOLLOW_FROMKW_in_payloadtypedecl1476 = frozenset([24])
    FOLLOW_EXTIDENTIFIER_in_payloadtypedecl1478 = frozenset([7])
    FOLLOW_ASKW_in_payloadtypedecl1480 = frozenset([40])
    FOLLOW_payloadtypename_in_payloadtypedecl1482 = frozenset([99])
    FOLLOW_99_in_payloadtypedecl1484 = frozenset([1])
    FOLLOW_94_in_messagesignature1536 = frozenset([40, 95])
    FOLLOW_payload_in_messagesignature1538 = frozenset([95])
    FOLLOW_95_in_messagesignature1540 = frozenset([1])
    FOLLOW_IDENTIFIER_in_messagesignature1559 = frozenset([94])
    FOLLOW_94_in_messagesignature1561 = frozenset([40, 95])
    FOLLOW_payload_in_messagesignature1563 = frozenset([95])
    FOLLOW_95_in_messagesignature1565 = frozenset([1])
    FOLLOW_payloadelement_in_payload1598 = frozenset([1, 96])
    FOLLOW_96_in_payload1601 = frozenset([40])
    FOLLOW_payloadelement_in_payload1603 = frozenset([1, 96])
    FOLLOW_payloadtypename_in_payloadelement1627 = frozenset([1])
    FOLLOW_parametername_in_payloadelement1644 = frozenset([1])
    FOLLOW_annotationname_in_payloadelement1664 = frozenset([98])
    FOLLOW_98_in_payloadelement1666 = frozenset([40])
    FOLLOW_payloadtypename_in_payloadelement1668 = frozenset([1])
    FOLLOW_annotationname_in_payloadelement1685 = frozenset([98])
    FOLLOW_98_in_payloadelement1687 = frozenset([40])
    FOLLOW_parametername_in_payloadelement1689 = frozenset([1])
    FOLLOW_globalprotocoldecl_in_protocoldecl1713 = frozenset([1])
    FOLLOW_localprotocoldecl_in_protocoldecl1718 = frozenset([1])
    FOLLOW_globalprotocolheader_in_globalprotocoldecl1731 = frozenset([102])
    FOLLOW_globalprotocoldefinition_in_globalprotocoldecl1733 = frozenset([1])
    FOLLOW_globalprotocolheader_in_globalprotocoldecl1750 = frozenset([44])
    FOLLOW_globalprotocolinstance_in_globalprotocoldecl1752 = frozenset([1])
    FOLLOW_GLOBALKW_in_globalprotocolheader1775 = frozenset([79])
    FOLLOW_PROTOCOLKW_in_globalprotocolheader1777 = frozenset([40])
    FOLLOW_protocolname_in_globalprotocolheader1779 = frozenset([94])
    FOLLOW_roledecllist_in_globalprotocolheader1781 = frozenset([1])
    FOLLOW_GLOBALKW_in_globalprotocolheader1796 = frozenset([79])
    FOLLOW_PROTOCOLKW_in_globalprotocolheader1798 = frozenset([40])
    FOLLOW_protocolname_in_globalprotocolheader1800 = frozenset([100])
    FOLLOW_parameterdecllist_in_globalprotocolheader1802 = frozenset([94])
    FOLLOW_roledecllist_in_globalprotocolheader1804 = frozenset([1])
    FOLLOW_94_in_roledecllist1823 = frozenset([85])
    FOLLOW_roledecl_in_roledecllist1825 = frozenset([95, 96])
    FOLLOW_96_in_roledecllist1828 = frozenset([85])
    FOLLOW_roledecl_in_roledecllist1830 = frozenset([95, 96])
    FOLLOW_95_in_roledecllist1834 = frozenset([1])
    FOLLOW_ROLEKW_in_roledecl1856 = frozenset([40])
    FOLLOW_rolename_in_roledecl1858 = frozenset([1])
    FOLLOW_ROLEKW_in_roledecl1873 = frozenset([40])
    FOLLOW_rolename_in_roledecl1875 = frozenset([7])
    FOLLOW_ASKW_in_roledecl1877 = frozenset([40])
    FOLLOW_rolename_in_roledecl1879 = frozenset([1])
    FOLLOW_100_in_parameterdecllist1900 = frozenset([86, 90])
    FOLLOW_parameterdecl_in_parameterdecllist1902 = frozenset([96, 101])
    FOLLOW_96_in_parameterdecllist1905 = frozenset([86, 90])
    FOLLOW_parameterdecl_in_parameterdecllist1907 = frozenset([96, 101])
    FOLLOW_101_in_parameterdecllist1911 = frozenset([1])
    FOLLOW_TYPEKW_in_parameterdecl1934 = frozenset([40])
    FOLLOW_parametername_in_parameterdecl1936 = frozenset([1])
    FOLLOW_TYPEKW_in_parameterdecl1954 = frozenset([40])
    FOLLOW_parametername_in_parameterdecl1956 = frozenset([7])
    FOLLOW_ASKW_in_parameterdecl1958 = frozenset([40])
    FOLLOW_parametername_in_parameterdecl1960 = frozenset([1])
    FOLLOW_SIGKW_in_parameterdecl1980 = frozenset([40])
    FOLLOW_parametername_in_parameterdecl1982 = frozenset([1])
    FOLLOW_SIGKW_in_parameterdecl2000 = frozenset([40])
    FOLLOW_parametername_in_parameterdecl2002 = frozenset([7])
    FOLLOW_ASKW_in_parameterdecl2004 = frozenset([40])
    FOLLOW_parametername_in_parameterdecl2006 = frozenset([1])
    FOLLOW_globalprotocolblock_in_globalprotocoldefinition2032 = frozenset([1])
    FOLLOW_INSTANTIATESKW_in_globalprotocolinstance2054 = frozenset([40])
    FOLLOW_membername_in_globalprotocolinstance2056 = frozenset([94])
    FOLLOW_roleinstantiationlist_in_globalprotocolinstance2058 = frozenset([99])
    FOLLOW_99_in_globalprotocolinstance2060 = frozenset([1])
    FOLLOW_INSTANTIATESKW_in_globalprotocolinstance2081 = frozenset([40])
    FOLLOW_membername_in_globalprotocolinstance2083 = frozenset([100])
    FOLLOW_argumentlist_in_globalprotocolinstance2085 = frozenset([94])
    FOLLOW_roleinstantiationlist_in_globalprotocolinstance2087 = frozenset([99])
    FOLLOW_99_in_globalprotocolinstance2089 = frozenset([1])
    FOLLOW_94_in_roleinstantiationlist2112 = frozenset([40])
    FOLLOW_roleinstantiation_in_roleinstantiationlist2114 = frozenset([95, 96])
    FOLLOW_96_in_roleinstantiationlist2117 = frozenset([40])
    FOLLOW_roleinstantiation_in_roleinstantiationlist2119 = frozenset([95, 96])
    FOLLOW_95_in_roleinstantiationlist2123 = frozenset([1])
    FOLLOW_rolename_in_roleinstantiation2145 = frozenset([1])
    FOLLOW_rolename_in_roleinstantiation2160 = frozenset([7])
    FOLLOW_ASKW_in_roleinstantiation2162 = frozenset([40])
    FOLLOW_rolename_in_roleinstantiation2164 = frozenset([1])
    FOLLOW_100_in_argumentlist2185 = frozenset([40, 94])
    FOLLOW_argument_in_argumentlist2187 = frozenset([96, 101])
    FOLLOW_96_in_argumentlist2190 = frozenset([40, 94])
    FOLLOW_argument_in_argumentlist2192 = frozenset([96, 101])
    FOLLOW_101_in_argumentlist2196 = frozenset([1])
    FOLLOW_messagesignature_in_argument2218 = frozenset([1])
    FOLLOW_messagesignature_in_argument2233 = frozenset([7])
    FOLLOW_ASKW_in_argument2235 = frozenset([40])
    FOLLOW_parametername_in_argument2237 = frozenset([1])
    FOLLOW_payloadtypename_in_argument2254 = frozenset([1])
    FOLLOW_payloadtypename_in_argument2269 = frozenset([7])
    FOLLOW_ASKW_in_argument2271 = frozenset([40])
    FOLLOW_parametername_in_argument2273 = frozenset([1])
    FOLLOW_parametername_in_argument2290 = frozenset([1])
    FOLLOW_parametername_in_argument2307 = frozenset([7])
    FOLLOW_ASKW_in_argument2309 = frozenset([40])
    FOLLOW_parametername_in_argument2311 = frozenset([1])
    FOLLOW_102_in_globalprotocolblock2337 = frozenset([11, 13, 15, 40, 45, 75, 80, 94, 103])
    FOLLOW_globalinteractionsequence_in_globalprotocolblock2339 = frozenset([103])
    FOLLOW_103_in_globalprotocolblock2341 = frozenset([1])
    FOLLOW_globalinteraction_in_globalinteractionsequence2361 = frozenset([1, 11, 13, 15, 40, 45, 75, 80, 94])
    FOLLOW_globalmessagetransfer_in_globalinteraction2385 = frozenset([1])
    FOLLOW_globalchoice_in_globalinteraction2390 = frozenset([1])
    FOLLOW_globalrecursion_in_globalinteraction2395 = frozenset([1])
    FOLLOW_globalcontinue_in_globalinteraction2400 = frozenset([1])
    FOLLOW_globalparallel_in_globalinteraction2405 = frozenset([1])
    FOLLOW_globalinterruptible_in_globalinteraction2410 = frozenset([1])
    FOLLOW_globaldo_in_globalinteraction2415 = frozenset([1])
    FOLLOW_message_in_globalmessagetransfer2429 = frozenset([25])
    FOLLOW_FROMKW_in_globalmessagetransfer2431 = frozenset([40])
    FOLLOW_rolename_in_globalmessagetransfer2433 = frozenset([89])
    FOLLOW_TOKW_in_globalmessagetransfer2435 = frozenset([40])
    FOLLOW_rolename_in_globalmessagetransfer2437 = frozenset([96, 99])
    FOLLOW_96_in_globalmessagetransfer2440 = frozenset([40])
    FOLLOW_rolename_in_globalmessagetransfer2442 = frozenset([96, 99])
    FOLLOW_99_in_globalmessagetransfer2447 = frozenset([1])
    FOLLOW_messagesignature_in_message2473 = frozenset([1])
    FOLLOW_parametername_in_message2478 = frozenset([1])
    FOLLOW_CHOICEKW_in_globalchoice2490 = frozenset([8])
    FOLLOW_ATKW_in_globalchoice2492 = frozenset([40])
    FOLLOW_rolename_in_globalchoice2494 = frozenset([102])
    FOLLOW_globalprotocolblock_in_globalchoice2496 = frozenset([1, 72])
    FOLLOW_ORKW_in_globalchoice2499 = frozenset([102])
    FOLLOW_globalprotocolblock_in_globalchoice2501 = frozenset([1, 72])
    FOLLOW_RECKW_in_globalrecursion2528 = frozenset([40])
    FOLLOW_recursionlabelname_in_globalrecursion2530 = frozenset([102])
    FOLLOW_globalprotocolblock_in_globalrecursion2532 = frozenset([1])
    FOLLOW_CONTINUEKW_in_globalcontinue2553 = frozenset([40])
    FOLLOW_recursionlabelname_in_globalcontinue2555 = frozenset([99])
    FOLLOW_99_in_globalcontinue2557 = frozenset([1])
    FOLLOW_PARKW_in_globalparallel2579 = frozenset([102])
    FOLLOW_globalprotocolblock_in_globalparallel2581 = frozenset([1, 4])
    FOLLOW_ANDKW_in_globalparallel2584 = frozenset([102])
    FOLLOW_globalprotocolblock_in_globalparallel2586 = frozenset([1, 4])
    FOLLOW_INTERRUPTIBLEKW_in_globalinterruptible2611 = frozenset([102])
    FOLLOW_globalprotocolblock_in_globalinterruptible2613 = frozenset([93])
    FOLLOW_WITHKW_in_globalinterruptible2615 = frozenset([102])
    FOLLOW_102_in_globalinterruptible2617 = frozenset([40, 94, 103])
    FOLLOW_globalinterrupt_in_globalinterruptible2620 = frozenset([40, 94, 103])
    FOLLOW_103_in_globalinterruptible2624 = frozenset([1])
    FOLLOW_INTERRUPTIBLEKW_in_globalinterruptible2646 = frozenset([40])
    FOLLOW_scopename_in_globalinterruptible2648 = frozenset([102])
    FOLLOW_globalprotocolblock_in_globalinterruptible2650 = frozenset([93])
    FOLLOW_WITHKW_in_globalinterruptible2652 = frozenset([102])
    FOLLOW_102_in_globalinterruptible2654 = frozenset([40, 94, 103])
    FOLLOW_globalinterrupt_in_globalinterruptible2657 = frozenset([40, 94, 103])
    FOLLOW_103_in_globalinterruptible2661 = frozenset([1])
    FOLLOW_message_in_globalinterrupt2687 = frozenset([9, 96])
    FOLLOW_96_in_globalinterrupt2690 = frozenset([40, 94])
    FOLLOW_message_in_globalinterrupt2692 = frozenset([9, 96])
    FOLLOW_BYKW_in_globalinterrupt2696 = frozenset([40])
    FOLLOW_rolename_in_globalinterrupt2698 = frozenset([99])
    FOLLOW_99_in_globalinterrupt2700 = frozenset([1])
    FOLLOW_DOKW_in_globaldo2727 = frozenset([40])
    FOLLOW_membername_in_globaldo2729 = frozenset([94])
    FOLLOW_roleinstantiationlist_in_globaldo2731 = frozenset([99])
    FOLLOW_99_in_globaldo2733 = frozenset([1])
    FOLLOW_DOKW_in_globaldo2756 = frozenset([40])
    FOLLOW_membername_in_globaldo2758 = frozenset([100])
    FOLLOW_argumentlist_in_globaldo2760 = frozenset([94])
    FOLLOW_roleinstantiationlist_in_globaldo2762 = frozenset([99])
    FOLLOW_99_in_globaldo2764 = frozenset([1])
    FOLLOW_DOKW_in_globaldo2785 = frozenset([40])
    FOLLOW_scopename_in_globaldo2787 = frozenset([98])
    FOLLOW_98_in_globaldo2789 = frozenset([40])
    FOLLOW_membername_in_globaldo2791 = frozenset([94])
    FOLLOW_roleinstantiationlist_in_globaldo2793 = frozenset([99])
    FOLLOW_99_in_globaldo2795 = frozenset([1])
    FOLLOW_DOKW_in_globaldo2816 = frozenset([40])
    FOLLOW_scopename_in_globaldo2818 = frozenset([98])
    FOLLOW_98_in_globaldo2820 = frozenset([40])
    FOLLOW_membername_in_globaldo2822 = frozenset([100])
    FOLLOW_argumentlist_in_globaldo2824 = frozenset([94])
    FOLLOW_roleinstantiationlist_in_globaldo2826 = frozenset([99])
    FOLLOW_99_in_globaldo2828 = frozenset([1])
    FOLLOW_localprotocolheader_in_localprotocoldecl2862 = frozenset([102])
    FOLLOW_localprotocoldefinition_in_localprotocoldecl2864 = frozenset([1])
    FOLLOW_localprotocolheader_in_localprotocoldecl2881 = frozenset([44])
    FOLLOW_localprotocolinstance_in_localprotocoldecl2883 = frozenset([1])
    FOLLOW_LOCALKW_in_localprotocolheader2904 = frozenset([79])
    FOLLOW_PROTOCOLKW_in_localprotocolheader2906 = frozenset([40])
    FOLLOW_protocolname_in_localprotocolheader2908 = frozenset([8])
    FOLLOW_ATKW_in_localprotocolheader2910 = frozenset([40])
    FOLLOW_rolename_in_localprotocolheader2912 = frozenset([94])
    FOLLOW_roledecllist_in_localprotocolheader2914 = frozenset([1])
    FOLLOW_LOCALKW_in_localprotocolheader2931 = frozenset([79])
    FOLLOW_PROTOCOLKW_in_localprotocolheader2933 = frozenset([40])
    FOLLOW_protocolname_in_localprotocolheader2935 = frozenset([8])
    FOLLOW_ATKW_in_localprotocolheader2937 = frozenset([40])
    FOLLOW_rolename_in_localprotocolheader2939 = frozenset([100])
    FOLLOW_parameterdecllist_in_localprotocolheader2941 = frozenset([94])
    FOLLOW_roledecllist_in_localprotocolheader2943 = frozenset([1])
    FOLLOW_localprotocolblock_in_localprotocoldefinition2967 = frozenset([1])
    FOLLOW_INSTANTIATESKW_in_localprotocolinstance2989 = frozenset([40])
    FOLLOW_membername_in_localprotocolinstance2991 = frozenset([94])
    FOLLOW_roledecllist_in_localprotocolinstance2993 = frozenset([99])
    FOLLOW_99_in_localprotocolinstance2995 = frozenset([1])
    FOLLOW_INSTANTIATESKW_in_localprotocolinstance3014 = frozenset([40])
    FOLLOW_membername_in_localprotocolinstance3016 = frozenset([100])
    FOLLOW_argumentlist_in_localprotocolinstance3018 = frozenset([94])
    FOLLOW_roledecllist_in_localprotocolinstance3020 = frozenset([99])
    FOLLOW_99_in_localprotocolinstance3022 = frozenset([1])
    FOLLOW_102_in_localprotocolblock3048 = frozenset([11, 13, 15, 40, 45, 75, 80, 94, 103])
    FOLLOW_localinteractionsequence_in_localprotocolblock3050 = frozenset([103])
    FOLLOW_103_in_localprotocolblock3052 = frozenset([1])
    FOLLOW_localinteraction_in_localinteractionsequence3072 = frozenset([1, 11, 13, 15, 40, 45, 75, 80, 94])
    FOLLOW_localsend_in_localinteraction3096 = frozenset([1])
    FOLLOW_localreceive_in_localinteraction3101 = frozenset([1])
    FOLLOW_localchoice_in_localinteraction3106 = frozenset([1])
    FOLLOW_localparallel_in_localinteraction3111 = frozenset([1])
    FOLLOW_localrecursion_in_localinteraction3116 = frozenset([1])
    FOLLOW_localcontinue_in_localinteraction3121 = frozenset([1])
    FOLLOW_localinterruptible_in_localinteraction3126 = frozenset([1])
    FOLLOW_localdo_in_localinteraction3131 = frozenset([1])
    FOLLOW_message_in_localsend3145 = frozenset([89])
    FOLLOW_TOKW_in_localsend3147 = frozenset([40])
    FOLLOW_rolename_in_localsend3149 = frozenset([96, 99])
    FOLLOW_96_in_localsend3152 = frozenset([40])
    FOLLOW_rolename_in_localsend3154 = frozenset([96, 99])
    FOLLOW_99_in_localsend3158 = frozenset([1])
    FOLLOW_message_in_localreceive3182 = frozenset([25])
    FOLLOW_FROMKW_in_localreceive3184 = frozenset([40])
    FOLLOW_IDENTIFIER_in_localreceive3186 = frozenset([99])
    FOLLOW_99_in_localreceive3188 = frozenset([1])
    FOLLOW_CHOICEKW_in_localchoice3212 = frozenset([8])
    FOLLOW_ATKW_in_localchoice3214 = frozenset([40])
    FOLLOW_rolename_in_localchoice3216 = frozenset([102])
    FOLLOW_localprotocolblock_in_localchoice3218 = frozenset([1, 72])
    FOLLOW_ORKW_in_localchoice3221 = frozenset([102])
    FOLLOW_localprotocolblock_in_localchoice3223 = frozenset([1, 72])
    FOLLOW_RECKW_in_localrecursion3250 = frozenset([40])
    FOLLOW_recursionlabelname_in_localrecursion3252 = frozenset([102])
    FOLLOW_localprotocolblock_in_localrecursion3254 = frozenset([1])
    FOLLOW_CONTINUEKW_in_localcontinue3275 = frozenset([40])
    FOLLOW_recursionlabelname_in_localcontinue3277 = frozenset([99])
    FOLLOW_99_in_localcontinue3279 = frozenset([1])
    FOLLOW_PARKW_in_localparallel3301 = frozenset([102])
    FOLLOW_localprotocolblock_in_localparallel3303 = frozenset([1, 4])
    FOLLOW_ANDKW_in_localparallel3306 = frozenset([102])
    FOLLOW_localprotocolblock_in_localparallel3308 = frozenset([1, 4])
    FOLLOW_INTERRUPTIBLEKW_in_localinterruptible3336 = frozenset([40])
    FOLLOW_scopename_in_localinterruptible3338 = frozenset([102])
    FOLLOW_localprotocolblock_in_localinterruptible3340 = frozenset([93])
    FOLLOW_WITHKW_in_localinterruptible3342 = frozenset([102])
    FOLLOW_102_in_localinterruptible3344 = frozenset([10, 103])
    FOLLOW_localcatch_in_localinterruptible3347 = frozenset([10, 103])
    FOLLOW_103_in_localinterruptible3351 = frozenset([1])
    FOLLOW_INTERRUPTIBLEKW_in_localinterruptible3375 = frozenset([40])
    FOLLOW_scopename_in_localinterruptible3377 = frozenset([102])
    FOLLOW_localprotocolblock_in_localinterruptible3379 = frozenset([93])
    FOLLOW_WITHKW_in_localinterruptible3381 = frozenset([102])
    FOLLOW_102_in_localinterruptible3383 = frozenset([88])
    FOLLOW_localthrow_in_localinterruptible3385 = frozenset([10, 103])
    FOLLOW_localcatch_in_localinterruptible3388 = frozenset([10, 103])
    FOLLOW_103_in_localinterruptible3392 = frozenset([1])
    FOLLOW_THROWSKW_in_localthrow3423 = frozenset([40, 94])
    FOLLOW_message_in_localthrow3425 = frozenset([89, 96])
    FOLLOW_96_in_localthrow3428 = frozenset([40, 94])
    FOLLOW_message_in_localthrow3430 = frozenset([89, 96])
    FOLLOW_TOKW_in_localthrow3434 = frozenset([40])
    FOLLOW_rolename_in_localthrow3436 = frozenset([96, 99])
    FOLLOW_96_in_localthrow3439 = frozenset([40])
    FOLLOW_rolename_in_localthrow3441 = frozenset([96, 99])
    FOLLOW_99_in_localthrow3445 = frozenset([1])
    FOLLOW_CATCHESKW_in_localcatch3474 = frozenset([40, 94])
    FOLLOW_message_in_localcatch3476 = frozenset([25, 96])
    FOLLOW_96_in_localcatch3479 = frozenset([40, 94])
    FOLLOW_message_in_localcatch3481 = frozenset([25, 96])
    FOLLOW_FROMKW_in_localcatch3485 = frozenset([40])
    FOLLOW_rolename_in_localcatch3487 = frozenset([99])
    FOLLOW_99_in_localcatch3489 = frozenset([1])
    FOLLOW_DOKW_in_localdo3516 = frozenset([40])
    FOLLOW_membername_in_localdo3518 = frozenset([94])
    FOLLOW_roleinstantiationlist_in_localdo3520 = frozenset([99])
    FOLLOW_99_in_localdo3522 = frozenset([1])
    FOLLOW_DOKW_in_localdo3545 = frozenset([40])
    FOLLOW_membername_in_localdo3547 = frozenset([100])
    FOLLOW_argumentlist_in_localdo3549 = frozenset([94])
    FOLLOW_roleinstantiationlist_in_localdo3551 = frozenset([99])
    FOLLOW_99_in_localdo3553 = frozenset([1])
    FOLLOW_DOKW_in_localdo3574 = frozenset([40])
    FOLLOW_scopename_in_localdo3576 = frozenset([98])
    FOLLOW_98_in_localdo3578 = frozenset([40])
    FOLLOW_membername_in_localdo3580 = frozenset([94])
    FOLLOW_roleinstantiationlist_in_localdo3582 = frozenset([99])
    FOLLOW_99_in_localdo3584 = frozenset([1])
    FOLLOW_DOKW_in_localdo3605 = frozenset([40])
    FOLLOW_scopename_in_localdo3607 = frozenset([98])
    FOLLOW_98_in_localdo3609 = frozenset([40])
    FOLLOW_membername_in_localdo3611 = frozenset([100])
    FOLLOW_argumentlist_in_localdo3613 = frozenset([94])
    FOLLOW_roleinstantiationlist_in_localdo3615 = frozenset([99])
    FOLLOW_99_in_localdo3617 = frozenset([1])
    FOLLOW_payloadtypename_in_synpred4_Scribble1107 = frozenset([1])
    FOLLOW_payloadtypename_in_synpred17_Scribble1627 = frozenset([1])
    FOLLOW_parametername_in_synpred18_Scribble1644 = frozenset([1])
    FOLLOW_annotationname_in_synpred19_Scribble1664 = frozenset([98])
    FOLLOW_98_in_synpred19_Scribble1666 = frozenset([40])
    FOLLOW_payloadtypename_in_synpred19_Scribble1668 = frozenset([1])
    FOLLOW_payloadtypename_in_synpred35_Scribble2254 = frozenset([1])
    FOLLOW_payloadtypename_in_synpred36_Scribble2269 = frozenset([7])
    FOLLOW_ASKW_in_synpred36_Scribble2271 = frozenset([40])
    FOLLOW_parametername_in_synpred36_Scribble2273 = frozenset([1])
    FOLLOW_parametername_in_synpred37_Scribble2290 = frozenset([1])
    FOLLOW_INTERRUPTIBLEKW_in_synpred71_Scribble3336 = frozenset([40])
    FOLLOW_scopename_in_synpred71_Scribble3338 = frozenset([102])
    FOLLOW_localprotocolblock_in_synpred71_Scribble3340 = frozenset([93])
    FOLLOW_WITHKW_in_synpred71_Scribble3342 = frozenset([102])
    FOLLOW_102_in_synpred71_Scribble3344 = frozenset([10, 103])
    FOLLOW_localcatch_in_synpred71_Scribble3347 = frozenset([10, 103])
    FOLLOW_103_in_synpred71_Scribble3351 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("ScribbleLexer", ScribbleParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
