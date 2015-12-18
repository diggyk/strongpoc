#!/usr/bin/env python

""" Command-line interface to StrongPOC."""

from __future__ import division

import argparse
import logging
import slumber
import sys
import textwrap
import traceback
import urllib

from strongpoc.version import __version__
from strongpoc.settings_client import settings

logging.getLogger("requests").setLevel(logging.WARNING)


def team_add(args):
    """ Add a new team

    Args:
        name: the new team name
    """
    api = slumber.API(settings.strongpoc_server)

    existing_team = api.teams.get(name=args.name)
    if existing_team:
        sys.exit("Team {} already exists!".format(args.name))

    new = api.teams.post({"name": args.name})

    if new:
        print "Created team {}".format(new["name"])
    else:
        sys.exit("Failed to create new team {}".format(args.name))


def team_list(args):
    """ List the existing teams

    Args:
        none
    """
    api = slumber.API(settings.strongpoc_server)

    teams = api.teams.get()

    if not teams:
        sys.exit("Error getting teams or no teams exist!")

    for team in teams:
        print team["name"]


def team_remove(args):
    """Remove an existing team

    Args:
        name: the name of the team to delete
    """
    api = slumber.API(settings.strongpoc_server)

    existing_team = api.teams.get(name=args.name)

    if not existing_team:
        sys.exit("Team {} not found!".format(args.name))
    if len(existing_team) > 1:
        sys.exit("Found more than one team when looking for {}!".format(
            args.name
        ))

    api.teams(existing_team[0]["id"]).delete()

    print "Removed team {}".format(args.name)


def team_rename(args):
    """Rename an existing team

    Args:
        oldname: the current name of the team
        newname: what the new name should be
    """
    api = slumber.API(settings.strongpoc_server)

    existing_team = api.teams.get(name=args.oldname)

    if not existing_team:
        sys.exit("Team {} not found!".format(args.oldname))
    if len(existing_team) > 1:
        sys.exit("Found more than one team when looking for {}!".format(
            args.oldname
        ))

    try:
        api.teams(existing_team[0]["id"]).put({
            "name": args.newname
        })
    except slumber.exceptions.HttpClientError as error:
        sys.exit(error.content)

    print "Renamed team {} to {}".format(args.oldname, args.newname)


def contact_type_add(args):
    """ Add a new contact type

    Args:
        name: the name of the new contact type
    """
    api = slumber.API(settings.strongpoc_server)

    contact_type = api.contact_types.get(name=args.name)
    if contact_type:
        sys.exit("Contact type {} already exists!".format(args.name))

    new = api.contact_types.post({"name": args.name})

    if new:
        print "Created contact type {}".format(new["name"])
    else:
        sys.exit("Failed to create new contact type {}".format(args.name))


def contact_type_list(args):
    """ List the existing contact types

    Args:
        none
    """
    api = slumber.API(settings.strongpoc_server)

    contact_types = api.contact_types.get()

    if not contact_types:
        sys.exit("Error getting contact types or no contact types exist!")

    for contact_type in contact_types:
        print contact_type["name"]


def contact_type_remove(args):
    """Remove an existing contact type

    Args:
        name: the name of the contact type to delete
    """
    api = slumber.API(settings.strongpoc_server)

    existing_contact_type = api.contact_types.get(name=args.name)

    if not existing_contact_type:
        sys.exit("Contact type {} not found!".format(args.name))
    if len(existing_contact_type) > 1:
        sys.exit("Found more than one contact type when looking for {}!".format(
            args.name
        ))

    api.contact_types(existing_contact_type[0]["id"]).delete()

    print "Removed contact_type {}".format(args.name)


def contact_type_rename(args):
    """Rename an existing contact type

    Args:
        oldname: the current name of the contact type
        newname: what the new name should be
    """
    api = slumber.API(settings.strongpoc_server)

    existing_contact_type = api.contact_types.get(name=args.oldname)

    if not existing_contact_type:
        sys.exit("Contact type {} not found!".format(args.oldname))
    if len(existing_contact_type) > 1:
        sys.exit("Found more than one contact type when looking for {}!".format(
            args.oldname
        ))

    try:
        api.contact_types(existing_contact_type[0]["id"]).put({
            "name": args.newname
        })
    except slumber.exceptions.HttpClientError as error:
        sys.exit(error.content)

    print "Renamed contact type {} to {}".format(args.oldname, args.newname)


def service_provider_add(args):
    """ Add a new service provider

    Args:
        name: the name of the new service provider
    """
    api = slumber.API(settings.strongpoc_server)

    service_provider = api.service_providers.get(name=args.name)
    if service_provider:
        sys.exit("Service provider {} already exists!".format(args.name))

    new = api.service_providers.post({"name": args.name})

    if new:
        print "Created service provider {}".format(new["name"])
    else:
        sys.exit("Failed to create new service provider {}".format(args.name))


def service_provider_list(args):
    """ List the existing service providers

    Args:
        none
    """
    api = slumber.API(settings.strongpoc_server)

    service_providers = api.service_providers.get()

    if not service_providers:
        sys.exit(
            "Error getting service providers or no service providers exist!"
        )

    for service_provider in service_providers:
        print service_provider["name"]


def service_provider_remove(args):
    """Remove an existing service provider

    Args:
        name: the name of the service provider to delete
    """
    api = slumber.API(settings.strongpoc_server)

    existing_service_provider = api.service_providers.get(name=args.name)

    if not existing_service_provider:
        sys.exit("Service provider {} not found!".format(args.name))
    if len(existing_service_provider) > 1:
        sys.exit("Found more than one service provider when looking for {}!".format(
            args.name
        ))

    api.service_providers(existing_service_provider[0]["id"]).delete()

    print "Removed service provider {}".format(args.name)


def service_provider_rename(args):
    """Rename an existing service provider

    Args:
        oldname: the current name of the service provider
        newname: what the new name should be
    """
    api = slumber.API(settings.strongpoc_server)

    existing_service_provider = api.service_providers.get(name=args.oldname)

    if not existing_service_provider:
        sys.exit("Service provider {} not found!".format(args.oldname))
    if len(existing_service_provider) > 1:
        sys.exit(
            "Found more than one service provider when looking for {}!".format(
                args.oldname
            )
        )

    try:
        api.service_providers(existing_service_provider[0]["id"]).put({
            "name": args.newname
        })
    except slumber.exceptions.HttpClientError as error:
        sys.exit(error.content)

    print "Renamed service provider {} to {}".format(args.oldname, args.newname)


def poc_add(args):
    """Add a new point of contact

    Args:
        team: name of the team for which this poc applies
        contact_type: the contact type we want to add
        service_provider: the name of the service provider for which this poc applies
        value: the actual value of the poc
    """
    api = slumber.API(settings.strongpoc_server)

    team = api.teams.get(name=args.team)

    if not team:
        sys.exit("Team {} not found!".format(args.team))

    contact_type = api.contact_types.get(name=args.contact_type)

    if not contact_type:
        sys.exit("Contact type {} not found!".format(args.contact_type))

    service_provider = api.service_providers.get(name=args.service_provider)

    if not service_provider:
        sys.exit("Service provider {} not found!".format(
            args.service_provider
        ))

    try:
        new = api.pocs.post({
            "team": team[0]["id"],
            "contact_type": contact_type[0]["id"],
            "service_provider": service_provider[0]["id"],
            "value": args.value
        })
    except slumber.exceptions.HttpClientError as error:
        sys.exit(error.content)

    print "Created new POC: {} can be reached by {} via {} at {}".format(
        args.team, args.service_provider, args.contact_type, args.value
    )


def poc_list(args):
    """List the existing points of contact

    Args:
        none
    """
    api = slumber.API(settings.strongpoc_server)

    pocs = api.pocs.get(expand=["teams","service_providers", "contact_types"])

    if not pocs:
        sys.exit("Error gettings POCs or not POCs exist!")

    for poc in pocs:
        print "{} can be reached by {} via {} at {}".format(
            poc["team"]["name"],
            poc["service_provider"]["name"],
            poc["contact_type"]["name"],
            poc["value"]
        )


def poc_remove(args):
    """Remove an existing POC

    Args:
        team: the name of the team whose POC we want to remove
        contact_type: the contact type of POC we want to remove
        service_provider: the service provider of POC we want to remove
    """
    api = slumber.API(settings.strongpoc_server)

    team = api.teams.get(name=args.team)

    if not team:
        sys.exit("Team {} not found!".format(args.team))

    contact_type = api.contact_types.get(name=args.contact_type)

    if not contact_type:
        sys.exit("Contact type {} not found!".format(args.contact_type))

    service_provider = api.service_providers.get(name=args.service_provider)

    if not service_provider:
        sys.exit("Service provider {} not found!".format(
            args.service_provider
        ))

    poc = api.pocs.get(
        team=team[0]["id"],
        contact_type=contact_type[0]["id"],
        service_provider=service_provider[0]["id"]
    )

    if not poc:
        sys.exit("Could not find a POC for {} {} {}".format(
            args.team, args.service_provider, args.contact_type
        ))

    api.pocs(poc[0]["id"]).delete()

    print "Deleted the POC for {} {} {}".format(
        args.team, args.service_provider, args.contact_type
    )


def poc_update(args):
    """Update the point of contact

    Args:
        team: the team whose POC we want to update
        contact_type: the type of contact we want to update
        service_provider: the service provider to which this POC applies
        value: the new value of the POC
    """
    api = slumber.API(settings.strongpoc_server)

    team = api.teams.get(name=args.team)

    if not team:
        sys.exit("Team {} not found!".format(args.team))

    contact_type = api.contact_types.get(name=args.contact_type)

    if not contact_type:
        sys.exit("Contact type {} not found!".format(args.contact_type))

    service_provider = api.service_providers.get(name=args.service_provider)

    if not service_provider:
        sys.exit("Service provider {} not found!".format(
            args.service_provider
        ))

    poc = api.pocs.get(
        team=team[0]["id"],
        contact_type=contact_type[0]["id"],
        service_provider=service_provider[0]["id"]
    )

    if not poc:
        sys.exit("Could not find a POC for {} {} {}".format(
            args.team, args.service_provider, args.contact_type
        ))

    try:
        api.pocs(poc[0]["id"]).patch({
            "value": args.value
        })
    except slumber.exceptions.HttpClientError as error:
        sys.exit(error.content)

    print "Updated: {} can be reached by {} via {} at {}".format(
        args.team, args.service_provider, args.contact_type, args.value
    )


def parse_cli_args():
    description_msg = "Strong Point of Contact CLI"
    parser = argparse.ArgumentParser(description=description_msg)

    parser.add_argument("-c", "--config", default="/etc/strongpoc/client.yaml",
                        help="Path to config file.")
    parser.add_argument(
        "-s", "--server", dest="strongpoc_server"
    )
    parser.add_argument(
        "--debug", action="count", default=0,
        help="Increase logging verbosity."
    )
    parser.add_argument(
        "-q", "--quiet", action="count", default=0,
        help="Decrease logging verbosity."
    )
    parser.add_argument("-V", "--version", action="version",
                        version="%%(prog)s %s" % __version__,
                        help="Display version information.")

    subparsers = parser.add_subparsers()

    # TEAM COMMANDS
    team_parser = subparsers.add_parser(
        "team", help="Create, list, edit and delete teams"
    )
    team_subparser = team_parser.add_subparsers()
    # add team line parser
    team_add_parser = team_subparser.add_parser("add")
    team_add_parser.add_argument("name", help="Team name")
    team_add_parser.set_defaults(func=team_add)
    
    # list teams line parser
    team_list_parser = team_subparser.add_parser("list")
    team_list_parser.set_defaults(func=team_list)

    # delete team line parser
    team_remove_parser = team_subparser.add_parser("remove")
    team_remove_parser.add_argument("name", help="Team name")
    team_remove_parser.set_defaults(func=team_remove)

    # rename team line parser
    team_rename_parser = team_subparser.add_parser("rename")
    team_rename_parser.add_argument("oldname", help="Existing team name")
    team_rename_parser.add_argument("newname", help="New team name")
    team_rename_parser.set_defaults(func=team_rename)

    # CONTACT_TYPE COMMANDS
    contact_type_parser = subparsers.add_parser(
        "ct", help="Create, list, edit and delete contact types"
    )
    contact_type_subparser = contact_type_parser.add_subparsers()
    # add contact_type line parser
    contact_type_add_parser = contact_type_subparser.add_parser("add")
    contact_type_add_parser.add_argument("name", help="Contact type name")
    contact_type_add_parser.set_defaults(func=contact_type_add)

    # list contact_types line parser
    contact_type_list_parser = contact_type_subparser.add_parser("list")
    contact_type_list_parser.set_defaults(func=contact_type_list)

    # remove contact_type line parser
    contact_type_remove_parser = contact_type_subparser.add_parser("remove")
    contact_type_remove_parser.add_argument("name", help="Contact type name")
    contact_type_remove_parser.set_defaults(func=contact_type_remove)

    # rename contact_type line parser
    contact_type_rename_parser = contact_type_subparser.add_parser("rename")
    contact_type_rename_parser.add_argument("oldname", help="Existing name")
    contact_type_rename_parser.add_argument("newname", help="New name")
    contact_type_rename_parser.set_defaults(func=contact_type_rename)

    # SERVICE_PROVIDER COMMANDS
    service_provider_parser = subparsers.add_parser(
        "sp", help="Create, list, edit and delete service providers"
    )
    service_provider_subparser = service_provider_parser.add_subparsers()
    # add service_provider line parser
    service_provider_add_parser = service_provider_subparser.add_parser("add")
    service_provider_add_parser.add_argument(
        "name", help="Service provider name"
    )
    service_provider_add_parser.set_defaults(func=service_provider_add)

    # list service_providers line parser
    service_provider_list_parser = service_provider_subparser.add_parser(
        "list"
    )
    service_provider_list_parser.set_defaults(func=service_provider_list)

    # remove service_provider line parser
    service_provider_remove_parser = service_provider_subparser.add_parser(
        "remove"
    )
    service_provider_remove_parser.add_argument(
        "name", help="Service provider name"
    )
    service_provider_remove_parser.set_defaults(func=service_provider_remove)

    # rename service_provider line parser
    service_provider_rename_parser = service_provider_subparser.add_parser(
        "rename"
    )
    service_provider_rename_parser.add_argument(
        "oldname", help="Existing name"
    )
    service_provider_rename_parser.add_argument("newname", help="New name")
    service_provider_rename_parser.set_defaults(func=service_provider_rename)

    # POCS COMMANDS
    poc_parser = subparsers.add_parser(
        "pocs",
        help="Create, list, edit and delete points of contact"
    )
    poc_subparser = poc_parser.add_subparsers()

    # add poc line parser
    poc_add_parser = poc_subparser.add_parser("add")
    poc_add_parser.add_argument("team", help="Team name")
    poc_add_parser.add_argument("service_provider", help="Service provider")
    poc_add_parser.add_argument("contact_type", help="Contact type")
    poc_add_parser.add_argument("value", help="Where to be contacted")
    poc_add_parser.set_defaults(func=poc_add)

    # list pocs line parser
    poc_list_parser = poc_subparser.add_parser("list")
    poc_list_parser.set_defaults(func=poc_list)

    # remove poc line parser
    poc_remove_parser = poc_subparser.add_parser("remove")
    poc_remove_parser.add_argument("team", help="Team name")
    poc_remove_parser.add_argument("service_provider", help="Service provider")
    poc_remove_parser.add_argument("contact_type", help="Contact type")
    poc_remove_parser.set_defaults(func=poc_remove)

    # update poc line parser
    poc_add_parser = poc_subparser.add_parser("update")
    poc_add_parser.add_argument("team", help="Team name")
    poc_add_parser.add_argument("service_provider", help="Service provider")
    poc_add_parser.add_argument("contact_type", help="Contact type")
    poc_add_parser.add_argument(
        "value", help="New value for where to be contacted"
    )
    poc_add_parser.set_defaults(func=poc_update)

    return parser.parse_args()


def main():
    args = parse_cli_args()
    # settings.update_from_config(args.config)

    if args.strongpoc_server:
        settings.strongpoc_server = args.strongpoc_server

    if args.debug:
        logging.basicConfig(level=logging.DEBUG, format=settings.log_format)
    elif args.quiet:
        logging.basicConfig(level=logging.ERROR, format=settings.log_format)
    else:
        logging.basicConfig(level=logging.INFO, format=settings.log_format)

    args.func(args)


if __name__ == "__main__":
    main()
