# Week 7 — Auth (~7 h)

**Manual:** [Authentication & authorization](../../src/content/chapters/04-authentication-and-authorization.mdx)

## Read (~2 h)

- Sessions vs JWT; where tokens live; RBAC basics.

## Type (~2 h)

- `POST /api/v1/auth/login` (fake user store is fine for learning).
- `Depends(get_current_user)` on mutating task routes.

## Exercise (~2 h)

1. Role **admin** vs **member**: only admin may DELETE.
2. Return **401** without token, **403** with insufficient role.
3. Note in README when you would swap in Auth0/Clerk at work.

## Done when

- [ ] All write routes protected.
- [ ] Tests cover 401 and 403.

## Commit message idea

`labs: week 7 — jwt auth and rbac on tasks`
