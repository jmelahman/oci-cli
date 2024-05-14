# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.marketplace_publisher.src.oci_cli_marketplace_publisher.generated import marketplace_publisher_service_cli


@click.command(cli_util.override('attachment.attachment_root_group.command_name', 'attachment'), cls=CommandGroupWithAlias, help=cli_util.override('attachment.attachment_root_group.help', """Use the Marketplace Publisher API to manage the publishing of applications in Oracle Cloud Infrastructure Marketplace."""), short_help=cli_util.override('attachment.attachment_root_group.short_help', """MarketplacePublisherService API"""))
@cli_util.help_option_group
def attachment_root_group():
    pass


@click.command(cli_util.override('attachment.attachment_group.command_name', 'attachment'), cls=CommandGroupWithAlias, help="""Description of Attachment.""")
@cli_util.help_option_group
def attachment_group():
    pass


@click.command(cli_util.override('attachment.attachment_collection_group.command_name', 'attachment-collection'), cls=CommandGroupWithAlias, help="""Results of a offers search. Contains boh AttachmentSummary items.""")
@cli_util.help_option_group
def attachment_collection_group():
    pass


marketplace_publisher_service_cli.marketplace_publisher_service_group.add_command(attachment_root_group)
attachment_root_group.add_command(attachment_group)
attachment_root_group.add_command(attachment_collection_group)


@attachment_group.command(name=cli_util.override('attachment.create_attachment.command_name', 'create'), help=u"""Creates a new Attachment. \n[Command Reference](createAttachment)""")
@cli_util.option('--file-base64-encoded', required=True, help=u"""Base64-encoded file to attach to the Offer. File must be a PDF with maximum size of 1 MB""")
@cli_util.option('--display-name', required=True, help=u"""The name used to refer to the uploaded data.""")
@cli_util.option('--type', required=True, help=u"""The type of offer attachment.""")
@cli_util.option('--offer-id', required=True, help=u"""unique Offer identifier""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace_publisher', 'class': 'Attachment'})
@cli_util.wrap_exceptions
def create_attachment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, file_base64_encoded, display_name, type, offer_id):

    if isinstance(offer_id, six.string_types) and len(offer_id.strip()) == 0:
        raise click.UsageError('Parameter --offer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['fileBase64Encoded'] = file_base64_encoded
    _details['displayName'] = display_name
    _details['type'] = type

    client = cli_util.build_client('marketplace_publisher', 'attachment', ctx)
    result = client.create_attachment(
        offer_id=offer_id,
        create_attachment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_attachment') and callable(getattr(client, 'get_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_attachment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@attachment_group.command(name=cli_util.override('attachment.delete_attachment.command_name', 'delete'), help=u"""Deletes a Attachment resource by identifier \n[Command Reference](deleteAttachment)""")
@cli_util.option('--offer-id', required=True, help=u"""unique Offer identifier""")
@cli_util.option('--attachment-id', required=True, help=u"""unique Offer identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "NEEDS_ATTENTION", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_attachment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, offer_id, attachment_id, if_match):

    if isinstance(offer_id, six.string_types) and len(offer_id.strip()) == 0:
        raise click.UsageError('Parameter --offer-id cannot be whitespace or empty string')

    if isinstance(attachment_id, six.string_types) and len(attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --attachment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace_publisher', 'attachment', ctx)
    result = client.delete_attachment(
        offer_id=offer_id,
        attachment_id=attachment_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds
                if 'opc-work-request-id' not in result.headers:
                    click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state')
                    cli_util.render_response(result, ctx)
                    return

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@attachment_group.command(name=cli_util.override('attachment.get_attachment.command_name', 'get'), help=u"""Gets a Attachment by identifier \n[Command Reference](getAttachment)""")
@cli_util.option('--offer-id', required=True, help=u"""unique Offer identifier""")
@cli_util.option('--attachment-id', required=True, help=u"""unique Offer identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace_publisher', 'class': 'Attachment'})
@cli_util.wrap_exceptions
def get_attachment(ctx, from_json, offer_id, attachment_id):

    if isinstance(offer_id, six.string_types) and len(offer_id.strip()) == 0:
        raise click.UsageError('Parameter --offer-id cannot be whitespace or empty string')

    if isinstance(attachment_id, six.string_types) and len(attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --attachment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace_publisher', 'attachment', ctx)
    result = client.get_attachment(
        offer_id=offer_id,
        attachment_id=attachment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@attachment_group.command(name=cli_util.override('attachment.get_attachment_content.command_name', 'get-attachment-content'), help=u"""Gets a Attachment content by identifier \n[Command Reference](getAttachmentContent)""")
@cli_util.option('--offer-id', required=True, help=u"""unique Offer identifier""")
@cli_util.option('--attachment-id', required=True, help=u"""unique Offer identifier""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_attachment_content(ctx, from_json, file, offer_id, attachment_id):

    if isinstance(offer_id, six.string_types) and len(offer_id.strip()) == 0:
        raise click.UsageError('Parameter --offer-id cannot be whitespace or empty string')

    if isinstance(attachment_id, six.string_types) and len(attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --attachment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace_publisher', 'attachment', ctx)
    result = client.get_attachment_content(
        offer_id=offer_id,
        attachment_id=attachment_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@attachment_collection_group.command(name=cli_util.override('attachment.list_attachments.command_name', 'list-attachments'), help=u"""Returns a list of Attachments. Requires either the BuyerCompartmentId or the SellerCompartmentId params. If neither or both are provided, then the API will return a 400. \n[Command Reference](listAttachments)""")
@cli_util.option('--offer-id', required=True, help=u"""unique Offer identifier""")
@cli_util.option('--buyer-compartment-id', help=u"""The ID of the buyer compartment this offer is associated with.""")
@cli_util.option('--seller-compartment-id', help=u"""The ID of the seller compartment this offer is associated with.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--id', help=u"""unique Offer identifier""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace_publisher', 'class': 'AttachmentCollection'})
@cli_util.wrap_exceptions
def list_attachments(ctx, from_json, all_pages, page_size, offer_id, buyer_compartment_id, seller_compartment_id, lifecycle_state, display_name, id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(offer_id, six.string_types) and len(offer_id.strip()) == 0:
        raise click.UsageError('Parameter --offer-id cannot be whitespace or empty string')

    kwargs = {}
    if buyer_compartment_id is not None:
        kwargs['buyer_compartment_id'] = buyer_compartment_id
    if seller_compartment_id is not None:
        kwargs['seller_compartment_id'] = seller_compartment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace_publisher', 'attachment', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_attachments,
            offer_id=offer_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_attachments,
            limit,
            page_size,
            offer_id=offer_id,
            **kwargs
        )
    else:
        result = client.list_attachments(
            offer_id=offer_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
