import React, { Component, Fragment } from 'react';
import ReactDom from "react-dom";
import { HashRouter as Router, Route, Switch, Redirect } from "react-router-dom";

import Header from "./Layout/Header";
import Dashboard from "./Course/Dashboard";

import Register from "./Accounts/Register";
import Login from "./Accounts/Login";

import { Provider } from "react-redux";
import store from "../store";

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <Router>
                    <Fragment>
                        <Header />
                        <div className="container">
                            <Switch>
                                <Route exact path="/" component={Dashboard} />
                                <Route exact path="/register" component={Register} />
                                <Route exact path="/login" component={Login} />
                            </Switch>
                        </div>
                    </Fragment>
                </Router>
            </Provider>
        )
    }
}

ReactDom.render(<App />, document.getElementById("app"));
