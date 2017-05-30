# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_Bowtie2(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def align_reads_to_assembly_app(self, params, context=None):
        """
        :param params: instance of type "AlignReadsParams" -> structure:
           parameter "reads_ref" of String, parameter "assembly_ref" of
           String, parameter "genome_ref" of String, parameter "output_name"
           of String, parameter "ws_id" of String, parameter "sampleset_id"
           of String, parameter "genome_id" of String, parameter
           "bowtie_index" of String, parameter "phred33" of String, parameter
           "phred64" of String, parameter "local" of String, parameter
           "very-fast" of String, parameter "fast" of String, parameter
           "very-sensitive" of String, parameter "sensitive" of String,
           parameter "very-fast-local" of String, parameter
           "very-sensitive-local" of String, parameter "fast-local" of
           String, parameter "fast-sensitive" of String
        :returns: instance of type "AlignReadsResult" -> structure: parameter
           "reads_alignment_ref" of String, parameter "report_name" of
           String, parameter "report_ref" of String
        """
        return self._client.call_method(
            'kb_Bowtie2.align_reads_to_assembly_app',
            [params], self._service_ver, context)

    def get_bowtie2_index(self, params, context=None):
        """
        :param params: instance of type "GetBowtie2Index" (Provide either a
           genome_ref or assembly_ref to get a Bowtie2 index for. output_dir
           is optional, if provided the index files will be saved in that
           directory.  If not, a directory will be generated for you and
           returned by this function.) -> structure: parameter "genome_ref"
           of String, parameter "assembly_ref" of String, parameter
           "output_dir" of String
        :returns: instance of type "GetBowtie2IndexResult" -> structure:
           parameter "output_dir" of String
        """
        return self._client.call_method(
            'kb_Bowtie2.get_bowtie2_index',
            [params], self._service_ver, context)

    def run_bowtie2_cli(self, params, context=None):
        """
        general purpose local function for running tools in the bowtie2 suite
        :param params: instance of type "RunBowtie2CLIParams" (supported
           commands: bowtie2 bowtie2-align-l bowtie2-align-s bowtie2-build
           bowtie2-build-l bowtie2-build-s bowtie2-inspect bowtie2-inspect-l
           bowtie2-inspect-s) -> structure: parameter "command_name" of
           String, parameter "options" of list of String
        """
        return self._client.call_method(
            'kb_Bowtie2.run_bowtie2_cli',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_Bowtie2.status',
                                        [], self._service_ver, context)