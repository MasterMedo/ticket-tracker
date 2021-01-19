import { useFormik } from 'formik';
import { useContext } from 'react';
import { AuthContext } from '../context';

export const Login = () => {
  const authContext = useContext(AuthContext);
  const formik = useFormik({
    initialValues: {
      username: '',
      password: '',
    },
    onSubmit: values => {
      authContext.login(values.username, values.password);
    },
  });

  return (
    <form onSubmit={formik.handleSubmit}
      className="block border rounded-2 m-2">
      <div>
        <input className="block ticket-form-title"
          id="username" name="username" type="string"
          placeholder="username"
          onChange={formik.handleChange}
          value={formik.values.username}
        />
      </div>
      <div>
        <input className="block ticket-form-title"
          id="password" name="password" type="string"
          placeholder="password"
          onChange={formik.handleChange}
          value={formik.values.password}
        />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};
