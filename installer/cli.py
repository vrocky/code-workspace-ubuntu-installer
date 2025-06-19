import argparse
from .utils import state
from .steps import install_node, install_python


def install(args):
    print(f'Installing profile {args.profile}')
    install_python.run()
    install_node.run()
    status = state.load_state()
    status['last_profile'] = args.profile
    state.save_state(status)


def resume(args):
    print('Resuming installation (placeholder)')


def retry(args):
    print(f'Retrying tool {args.tool} (placeholder)')


def show_status(args):
    print('Current status:')
    print(state.load_state())


def main(argv=None):
    parser = argparse.ArgumentParser(prog='code-workspace-ubuntu-installer')
    subparsers = parser.add_subparsers(dest='command')

    p_install = subparsers.add_parser('install')
    p_install.add_argument('--profile', default='full')
    p_install.set_defaults(func=install)

    p_resume = subparsers.add_parser('resume')
    p_resume.set_defaults(func=resume)

    p_retry = subparsers.add_parser('retry')
    p_retry.add_argument('--tool', required=True)
    p_retry.set_defaults(func=retry)

    p_status = subparsers.add_parser('status')
    p_status.set_defaults(func=show_status)

    args = parser.parse_args(argv)
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
