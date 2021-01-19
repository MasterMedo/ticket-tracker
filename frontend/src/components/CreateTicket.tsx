import { useFormik } from 'formik';
import { useEffect, useState } from 'react';
import { Category } from '../models/Category';

export const CreateTicket = () => {
  const [categories, setCategories] = useState<Category[]>([]);

  useEffect (() => {
    fetch("/categories")
      .then(r => r.json())
      .then((data: Category[]) => {
        setCategories(data);
      });
  }, []);

  const formik = useFormik({
    initialValues: {
      title: '',
      category: '',
      content: '',
    },
    onSubmit: values => {
      fetch(`/tickets`, {
        method: "POST",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(values, null, 2)});
    },
  });
  return (
    <form onSubmit={formik.handleSubmit}
      className="block border rounded-2 m-2">
      <select
        name="category"
        onChange={formik.handleChange}
        value={formik.values.category}
      >
        {categories.map(category =>
          <option key={category.id}
            label={category.name}
            value={JSON.stringify(category)}
          />
        )}
      </select>
      <div>
        <input className="block ticket-form-title"
          id="title" name="title" type="string"
          placeholder="Title"
          onChange={formik.handleChange}
          value={formik.values.title}
        />
      </div>
      <div className="ticket-form-content-parent">
        <textarea className="ticket-form-content"
          id="content" name="content"
          placeholder="content"
          onChange={formik.handleChange}
          value={formik.values.content}
        />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};
