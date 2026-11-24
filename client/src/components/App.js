import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import NavBar from "./NavBar";
import Login from "../pages/Login";
import RecipeList from "../pages/RecipeList";
import NewRecipe from "../pages/NewRecipe";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // auto-login
    // fetch("/check_session").then((r) => {
    fetch("/me", {
      headers: {
        "Authorization": `Bearer ${localStorage.getItem("token")}`
      }
    }).then((r) => {
      if (r.ok) {
        r.json().then((user) => setUser(user));
      }
    });
  }, []);
  // pass onLogin to Login component
  const onLogin = (token, user) => {
    localStorage.setItem("token", token);
    setUser(user);
  };

  // if (!user) return <Login onLogin={setUser} />;
  if (!user) return <Login onLogin={onLogin} />;

  return (
    <>
      <NavBar user={user} setUser={setUser} />
      <main>
        <Switch>
          <Route path="/new">
            <NewRecipe user={user} />
          </Route>
          <Route path="/">
            <RecipeList />
          </Route>
        </Switch>
      </main>
    </>
  );
}

export default App;
