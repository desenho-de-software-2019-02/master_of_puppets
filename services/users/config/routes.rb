Rails.application.routes.draw do
  get 'registrations/create'
  devise_for :users,
             controllers: {
               sessions: 'sessions',
               registrations: 'registrations',
               users: 'users'
             }
  # devise_for :users
end
