import React, { Component } from 'react';
import { connect } from 'react-redux';
import reactMixin from 'react-mixin';
import { Link, Lifecycle } from 'react-router';

import { updateDocTitle } from 'actions/App/AppActions';
import { fetchHierarchy } from 'actions/App/BreadCrumbActions';

import AccountForm from 'components/Accounts/AccountForm/AccountForm';

@reactMixin.decorate(Lifecycle)
class AccountEditPage extends Component {
  constructor(props) {
    super(props);
    this.routerWillLeave = this.routerWillLeave.bind(this);
  }

  componentWillMount() {
    this.fetchAccountDetails(this.props);
  }

  componentWillReceiveProps(nextProps) {
    if (nextProps.params.accountId !== this.props.params.accountId) {
      this.fetchAccountDetails(nextProps);
    }
  }

  render() {
    let output = (<div/>);

    if(this.props.Account.details){
      output = (
        <div>
          <div className="form-module">
            <div className="form-module-header">Edit Account - {this.props.Account.details.name}</div>
            <div className="form-module-body">
              { (this.props.Account.details.id !== undefined)
                ? <AccountForm editMode={true} {...this.props} />
                : null
              }
            </div>
          </div>
        </div>
      );
    }

    return output;
  }

  routerWillLeave(nextLocation) {
    if(this.props.App.formChanged){
      return 'Your progress is not saved. Are you sure you want to leave?';
    }
  }

  fetchAccountDetails(props) {
    const { dispatch } = props;

    updateDocTitle('Edit Account');

    dispatch(fetchHierarchy('account', props))
      .catch(function(){
        props.history.replaceState(null, '/error404');
      })
      .then(() => {
        if(this.props.Account.details){
          updateDocTitle('Edit Account - ' + this.props.Account.details.name);
        }
      });
  }
}

AccountEditPage.propTypes = {};

// Which props do we want to inject, given the global state?
function select(state) {
  return {
    Account: state.Account,
    App: state.App
  };
}

// Wrap the component to inject dispatch and state into it
export default connect(select)(AccountEditPage);
